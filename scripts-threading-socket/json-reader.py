import json

#print(dir(json))

jsonString='''\
[
    {"Name":"Vivek","Email":"vivek@conceptarchitect.in","phone":[{"number":"9036084835","type":"m"},{"number":"9036084100","type":"jio"}]},
    {"Name":"Shweta","Email":"shweta@conceptarchitect.in"},
    {"Name":"Aditi","Email":"aditi@conceptarchitect.in"}
]

'''

pyJson= json.loads(jsonString)

print(pyJson)