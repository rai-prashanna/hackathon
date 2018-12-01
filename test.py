import json
from pprint import pprint

# wholedata=""
# with open('bmd007.json', 'r') as myfile:
#     data=myfile.read().replace("\'", "\"")
#     wholedata=wholedata+data


import json
from pprint import pprint

with open('bmd007.json') as f:
    data = json.load(f)

result=data['experiences']
if 'experiences' in data:
    jobs=data['experiences']
    pprint(result['jobs'])

