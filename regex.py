import re

handle = open("mbox-short.txt")
for line in handle:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
        
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
