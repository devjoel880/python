import json
data = '''
{
    "name" : "Chuck",
    "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
    },
    "email" : {
    "hide" : "yes"
    }
}'''

# info is now a dictionary with key/value
info = json.loads(data) #xml fromstring(data)
print('Name:',info["name"])
print('Hide:', info["email"]["hide"])
print('Phone:', info["phone"]["number"])
