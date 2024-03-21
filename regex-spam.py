# Search for the spam cofidence in an email. Extract the spam coonfidence. Check the largest spam confidence value

import re

fhand = open('mbox-short.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
    
#print(numlist)
print('Maximum:', max(numlist))