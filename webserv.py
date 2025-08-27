import xml.etree.ElementTree as ET
import urllib.request

data = '''
<person>
<name>Chuck</name>
<phone type="intl">+1 734 303 4456</phone>
<email hide="yes"/>
</person>
'''

input = '''
<stuff>
<users>
<user x="2"><id>001</id><name>Chuck</name></user>
<user x="7"><id>009</id><name>Brent</name></user>
</users>
</stuff>
'''

tree = ET.fromstring(data)
print(f"Name: {tree.find('name').text}")
print(f"Phone: {tree.find('phone').text} {tree.find('phone').get('type')}")
print(f"Attr: {tree.find('email').get('hide')}")

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') 
print(f"User count: {len(lst)}")
for item in lst:
    print(f"Name: {item.find('name').text}")
    print(f"Id: {item.find('id').text}")
    print(f"Attr: {item.get('x')}")




url = 'http://py4e-data.dr-chuck.net/comments_2285828.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))
