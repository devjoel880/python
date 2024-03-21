# use either mbox.txt or mbox-short.txt
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Cannot open file: ', fname)
    quit()

count = 0
for line in fhand :
    if line.startswith('Subject:'):
        count = count+ 1
print('There were', count, 'subject lines in', fname)
