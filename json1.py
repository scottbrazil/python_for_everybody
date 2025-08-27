import json
import ssl 
import urllib.request, urllib.parse

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

info = json.loads(data)
print(f"Name: {info["name"]}")
print(f"Hide: {info["email"]["hide"]}")

data = '''
[
  { "id":"001", "x":"2", "name":"Chuck" } ,
  { "id":"009", "x":"7", "name":"Brent" }
]'''

info = json.loads(data)
print(f"User count: {len(info)}")

for item in info:
    print(f"Name {item['name']}")
    print(f"Id {item['id']}")
    print(f"Attribute {item['x']}")

url = 'http://py4e-data.dr-chuck.net/comments_2285829.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)
print(f"Count {len(js['comments'])}")
sum = 0
for item in js['comments']:
    sum = sum + int(item['count'])
print(f"Sum: {sum}")