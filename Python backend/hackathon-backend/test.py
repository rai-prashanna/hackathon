import json

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

skills=[
    "Java",
    "HTML",
    "Android",
    "Java Enterprise Edition",
    "Android Development",
    "Drupal",
    "Hibernate",
    "Spring Framework",
    "CSS",
    "Volleyball",
    "Raspberry Pi",
    "Object Oriented Design",
    "JSF",
    "JavaFX",
    "Java Web Services",
    "Primefaces",
    "Apache Derby",
    "Spring Boot",
    "Groovy Grails",
    "Spring Security",
    "Microservices",
    "CQRS",
    "Groovy",
    "Apache Kafka"
]

print(keyword_search('test.json', skills[1]))



