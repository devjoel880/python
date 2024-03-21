import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter link - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
number_list = list()

for tag in tags:
    # Find all occurrences of digits in the content of the span tag ('tag.get_text()')
    numbers = re.findall('[0-9]+', tag.get_text())
    if numbers:
        for num in numbers:
            num = int(num)
            number_list.append(num)
            
total = sum(number_list)
print(total)        