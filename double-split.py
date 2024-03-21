fhand = open('txt.txt')
for line in fhand:
    words = line.split()
    email = words[1]
    ss = email.split('@')
    
print(words)
print(ss[1])

