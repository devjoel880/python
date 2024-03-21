data = 'From stephen.marquard@uct.ac.za Sat Jan  5  09:14:16 2008'
atpos = data.find('@')
print(atpos)

spos = data.find(' ', atpos)
print(spos)

host = data[atpos : spos]
print(host)