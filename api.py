from flask import Flask, flash, render_template, redirect, url_for, request, session
from flask_restful import reqparse, abort, Api, Resource
import json
from pprint import pprint
import os

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
api = Api(app)


class Linkedin(Resource):
    def get(self,id,item):
        os.system("scrapeli --user "+id+" -o prai.json")
        with open('prai.json') as f:
            data = json.load(f)
            # print(data)
            if int(item) ==0:
                if 'experiences' in data:
                    experiences=data['experiences']
                    # print(experiences)
                    if 'jobs' in experiences:
                        jobs=experiences['jobs']
                        # print(jobs)
                        return jobs,201
            if int(item)==1:
                if 'skills' in data:
                    skills=data['skills']
                    # print(skills)
                    return skills,201




##
## Actually setup the Api resource routing here
##

api.add_resource(Linkedin, '/extract/<id>/<item>')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8181)


