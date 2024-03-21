print('Create an Account today!')

fn = input('Enter your full name: ')
user = input('Choose username: ')
pwd = input('Choose secure password: ')

credentials = list()
credentials.append(fn)
credentials.append(user)
credentials.append(pwd)

print('All Done')
print(credentials[1])                                         