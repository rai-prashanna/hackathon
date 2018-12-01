from flask import Flask, flash, render_template, redirect, url_for, request, session
from flask_restful import reqparse, abort, Api, Resource
import json
from pprint import pprint
import os

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
api = Api(app)


def keyword_search(path, keywordlist, limit = 5):
    json_data = json_dump_opener(path)
    job_list = jobs_of_keyword(json_data, keywordlist)
    employer_list = employer_aggregation(job_list)

    return employer_sort(employer_list['Employers'], limit)

def jobs_of_keyword(data, keywordlist):
    JOBS = {}

    for job in data:
        desc = job['PLATSBESKRIVNING'].lower()
        jobb_id = job['PLATSNUMMER']
        job_employer = job['AG_NAMN']
        job_posted = job['FORSTA_PUBLICERINGSDATUM']
        job_title = job['PLATSRUBRIK']
        job_yrke = job['YRKE_ID']
        skill_found = True

        for n, key in enumerate(keywordlist):
            if key.lower() not in desc:
                skill_found &= False
            else:
                skill_found &= True

        if skill_found:
            JOBS[jobb_id] = {
                'DatePosted' : job_posted,
                'Title': job_title,
                'EmployerName': job_employer,
                'YrkeId': job_yrke
            }

    return JOBS

def employer_aggregation(job_list):
    TOP_EMPLOYERS = {
        'Employers' : {},
        'LastPosted' : {}
    }

    for job in job_list:
        employer = job_list[job]['EmployerName']
        if employer in TOP_EMPLOYERS['Employers']:
            TOP_EMPLOYERS['Employers'][employer] += 1
            date = job_list[job]['DatePosted']
            if date > TOP_EMPLOYERS['LastPosted'][employer]:
                 TOP_EMPLOYERS['LastPosted'][employer] = date
        else:
            TOP_EMPLOYERS['Employers'][employer] = 1
            date = job_list[job]['DatePosted']
            TOP_EMPLOYERS['LastPosted'][employer] = date
    return TOP_EMPLOYERS

def employer_sort(mydict, limit = 5):
    return {key: mydict[key] for key in sorted(mydict, key=mydict.get, reverse=True)[:limit]}

def last_posted(mydict, employer):
    return mydict[employer]


def json_dump_opener(path):
    with open(path) as f:
        json_data = []
        line = f.readline()
        id = 0
        while line:
            json_data.append(json.loads(line))
            line = f.readline()
            id += 1
        return json_data

class Linkedin(Resource):
    def get(self,id,item):
        os.system("scrapeli --user "+id+" -o prai.json")
        with open('prai.json') as f:
            data = json.load(f)
            # print(data)
            # if int(item) ==0:
            #     if 'experiences' in data:
            #         experiences=data['experiences']
            #         # print(experiences)
            #         if 'jobs' in experiences:
            #             jobs=experiences['jobs']
            #             # print(jobs)
            #             return jobs,201
            # if int(item)==1:
            #     if 'skills' in data:
            #         skills=data['skills']
            #         # print(skills)
            #         return skills,201
            list_of_skills=[]
            if 'skills' in data:
                    skills=data['skills']
                    for skill in skills:
                        single_skill=skill['name']
                        list_of_skills.append(single_skill)

            result=keyword_search('test.json', list_of_skills[0])
            return result,201







##
## Actually setup the Api resource routing here
##

api.add_resource(Linkedin, '/extract/<id>/<item>')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8181)



