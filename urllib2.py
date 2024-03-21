# The library that does all the socket works URLLIB

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
bigcount = None
bigword = None

for key, value in counts.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key
        
print('Bigword:', bigword, ':-', bigcount)
