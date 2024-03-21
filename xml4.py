# Use the link : http://py4e-data.dr-chuck.net/comments_1963974.xml

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
html = urllib.request.urlopen(url, context=ctx).read()

stuff = ET.fromstring(html)
comments = stuff.findall('comments/comment')

ct = 0
count = 0
lst = list()
print('Retrieving', url)

for comment in comments:
    cm = comment.find('count').text
    cm = int(cm)
    lst.append(cm)

for cnt in lst:
    count += 1

for i in html:
    ct = ct + 1

print('Retrieved', ct, 'characters')
print('Count:', count)
print(sum(lst))
