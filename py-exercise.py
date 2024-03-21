# Convert elevator floors
"""
inp = input("Europe floor?")
usf = int(inp) + 1
print('US floor', usf)
"""
# try/catch conditional statement
number = input("Enter a number: ")
try:
    ival = int(number)
except:
    ival = -1
if ival > 0 :
    print('Nice work!')
else : 
    print('Not a number!')