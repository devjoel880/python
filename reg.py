# Look for characters starting with 'from:', and extract those without whitespace and also contains '@'

import re

handle = open('mbox-short.txt')
count = 0
for line in handle:
    line = line.rstrip()
    fd = re.findall('^From:\s(\S+@\S+)', line) 
    if fd:
        count += 1
        print(fd[0])
print('Count: ', count, 'email addresses')
