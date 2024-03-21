# Resume generator software developed by Dev-Joel
# Programming Language: Python

print('Enter your personal details below\n>>')

name = input('>> Enter your full name: ')
age = input('>> How old are you? : ')
phone = input('>> Enter your phone numbers (separated by commas): ')
email = input('>> Email address: ')
address = input('>> Home address: ')

# prompt for additional information
education = input('>> Highest level of education completed: ')
certificate = input('>> Enter certification (separated by commas): ')
experience = input('>> Work eperience: ')
skill = input('Skills acquired: ')

# Print resume
print("Full Name: ", name)
print("Age: ", age)
print("Phones: ", phone)
print("Email : ", email)
print("Address: ", address)

# Print additional info if provided
if education != "":
    print("Education: ", education)
if certificate != "":
    print("Certifications: ", certificate)
if experience != "":
    print("Work Experience: ", experience)
if skill != "":
    print("Skills: ", skill)

print('Resume generated for', name)