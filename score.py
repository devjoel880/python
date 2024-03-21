#Program to prommpt for a score between 0.0 and 1.0
score = input("Enter Score: ")

try:
    fs = float(score)
except:
    print("Error, please input a number!")
    quit()

if fs > 1.0:
    print('Error, out of range')
    quit()
elif fs >= 0.9:
    print('A')
elif fs >= 0.8:
    print('B')
elif fs >= 0.7:
    print('C')
elif fs >= 0.6:
    print('D')
else:
    print('F')