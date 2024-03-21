import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter link: ')
count = input('Enter count: ')
pos = input('Enter position: ')

try:
    count_x = int(count)
    pos_x = int(pos)
except ValueError:
    print('Please input numeric value only')
    exit()

for _ in range(count_x):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
    # Check if the position is within the range of available links
    if pos_x < len(tags):
        # Updating the value of 'url' so it follows the next link at the specified position
        url = tags[pos_x].get('href')
        print('Retrieving:', url)
    else:
        print(f'Position {pos_x} is out of range. Exiting loop.')
        break
