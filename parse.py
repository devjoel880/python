fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
    
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith('From '):
        split_line = line.split()
        count += 1
        print(split_line[1])
        
print('There were', count, 'lines in the file with From as the first word')
        
        