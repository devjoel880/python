import xml.etree.ElementTree as ET

input_data = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input_data)
users = stuff.findall('users/user')
print('User count: ', len(users))

count = 0
for user in users:
    count += 1
    print('User', count, ':')
    print('Name:', user.find('name').text)
    print('ID:', user.find('id').text)
    print('Attr:', user.get('x'))
    print()  # Empty line for better readability between users
