import json
from pprint import pprint

# wholedata=""
# with open('bmd007.json', 'r') as myfile:
#     data=myfile.read().replace("\'", "\"")
#     wholedata=wholedata+data


import json
from pprint import pprint
import os

os.system("scrapeli --user bmd007 -o prai.json")

# with open('bmd007.json') as f:
#     data = json.load(f)
#
# print("experiences are ::.............")
# if 'experiences' in data:
#     experiences=data['experiences']
#     if 'jobs' in experiences:
#         jobs=experiences['jobs']
#         for item in jobs:
#             print(item['date_range'])
#             print(item['title'])
#             print("*******")
#
# print("skills are ::.............")
# if 'skills' in data:
#     skills=data['skills']
#     for item in skills:
#             print(item['name'])
#             print("*******")
#
