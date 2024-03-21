# Code that reads a file, and arranges it into a list

fname = input('Enter the file name: ')
fhand = open(fname)
ls = list()

for line in fhand:
    words = line.split()    
    for word in words:
        if word not in ls:
            ls.append(word)
     
ls.sort()
print(ls)
        