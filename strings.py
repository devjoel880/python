fName = input('Enter Full Name: ')
gnd = input('Gender: ')

if gnd[0].lower() == 'm' :
    greet = 'Hello, Mr.' + fName
    print(greet)
elif gnd[0].lower() == 'f' :
    greet = 'Hello, Mrs.' + fName
    print(greet)