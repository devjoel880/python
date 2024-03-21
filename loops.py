"""
# While loop. Can also be infinite if the iteration value is not defined.
n = 5
while n > 0 :
    print(n)
    n = n -1
print('Blastoff!')

#For loop (definite loops)
friends = ['Gbolahan', 'Joel', 'Adeoye']
for friend in friends :
    print("Hello: ", friend)
    print('>>')
print('Done!')

# the 'break' and 'continue' keyword are used in loops to either exit the loop or restart the loop

n = 9
while n > 0:
    print(n)
    n = n - 1
    if n == 4:
        continue
        
#.....................

largest = -1
print('Before', largest)
for the_num in [3, 12, 42, 79, 15]:
    if the_num > largest:
        largest = the_num
        print(largest, the_num)
print('After', largest)
#......................
count = 0
print('Before', count)
for thing in [8, 45, 12, 62, 3, 74] :
    count += 1
    print(count, thing)
print('After', count)
#..................
found = False
for value in [8, 6, 3, 15, 1, 22] :
    found = True
    if value == 3 :
        print(found)
print('All done!')
#......................

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
#.................

j = None

for x in [10, 88, 2, 46, 93, 12]:
    if j is None:
        j = x
    elif x < j:
        j = x
    print(j, x)

print('All done!...', 'The smallest value in the array is: ', j)
#...............
sm = -1
for th in [9,41,12,3,74,15]:
    if th < sm:
        sm = th
print(sm)
#..................................

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

"""


fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1