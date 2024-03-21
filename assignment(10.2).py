fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)
hour = list()
fhour = dict()

for line in fhand:
    if line.startswith('From '):
        line_split = line.split()
        time = line_split[5]
        hour.append(time.split(':')[0])
        
for each in hour:
    fhour[each] = fhour.get(each, 0) + 1


for key, value in sorted(fhour.items()):
    print(key, value)