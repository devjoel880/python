import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter link - ')
for y in range(10):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # Updating the value of 'URL' so it follows the next link at the second position
    url = tags[2].get('href')
    print('Retrieving: ' , url)
