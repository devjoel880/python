import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL - ')

for x in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup('a')
    # update the url variable and make it go to the next link in the loop (range)
    url = links[17].get('href')
    print('Retrieving:', url)
