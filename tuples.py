fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
ls = list()
for key, val in counts.items():
    newtup = (val, key)
    ls.append(newtup)
 
#sorting lists in reversed order
ls = sorted(ls, reverse=True)

# slicing with loops
for val, key in ls[:10]:
    print(key, val)
    
    
#print(sorted([(v,k) for k,v in d.items()]))