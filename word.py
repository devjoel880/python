# use words.txt
fname = input('Enter the file name: ')

fhand = open(fname)

fread = fhand.read()
fread = fread.strip()
print(fread.upper())