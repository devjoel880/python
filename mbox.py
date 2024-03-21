# parsing strings and extracting outputs

fname = input('Enter file name: ')
fhand = open(fname)
count = 0


for line in fhand:
    l = line.split()
    if line.startswith('from'):
        count += 1
        
print(l)
        