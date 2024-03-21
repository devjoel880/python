numlist = list()

while True:
    inp = input('Enter a number:  ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    
avg = sum(numlist) / len(numlist)
print('Average:',  avg)    