#Loop through a mailbox file (mbox-short)
#Find the sender that sent the largest emails

name = input('Enter file: ')
if len(name) < 1:
    name = "mbox-short.txt"
fhand = open(name)
collection = dict()
ls = list()

for line in fhand:
    if line.startswith('From '):
        l_s = line.split()
        ls.append(l_s[1])
        
for word in ls:
    collection[word] = collection.get(word, 0) + 1
    
bigcount = None
bigsender = None

for aa,bb in collection.items():
    if bigcount is None or bb > bigcount:
        bigcount = bb
        bigsender = aa
        
print(bigsender, bigcount)

print("Yay!!", bigsender, "sent an email", bigcount, "times")