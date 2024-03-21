fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    if line.lower().startswith('from:'):
        count = count + 1
        print(line)
print('Lines: ', count)