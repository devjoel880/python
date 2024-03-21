"""

# Program to prompt a user for input and return the Maximum and Minimun number using an indefinite loop

largest = None
smallest = None

while True:
    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        num = int(num)
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
        if largest < num:
            largest = num
        if smallest > num:
            smallest = num
    except:
        print('Invalid input')
        
if largest is not None:
    print('Maximum', largest)
if smallest is not None:
    print('Minimum', smallest)
##################################
x = "From marquard@uct.ac.za"
print(x[14:17])
##################################
print(len('banana')*7)
#############################3


fruit = "banana"
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print('The letter a in the fruit "banana" appeard', count, "times")

#################################3

"""
fruit = "banana"
pos = fruit.find('n')
print(pos)
