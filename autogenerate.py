# Auto-generate passwords from user input

print('Welcome to the registration portal!')
fname = input("Enter first name: ")
lname = input('Enter last name: ')

while True:
    age = input('Enter age: ')
    try:
        age = int(age)
        break
    except:
        print('Please input a numeral character')


gender = input('Gender: ')

# Generate password
uname = fname[0:3].lower() + lname[-3:].lower()
uname = uname.capitalize()
print('Enter password securely.....')


while True:
    pwd = input('>> ')
    if len(pwd) < 6:
        print('Password should be at least 6 characters!')
    else:
        print('Successfully registered ', fname, lname, 'as: ', uname)
        break