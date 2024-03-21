# Program to calculate the overtime for workers who worked for over 40 hours.
hrs = input('enter hours: ')
h = float(hrs)
rate = input('enter rate: ')
r = float(rate)

if h <= 40 :
    pay = h * r
    print(pay)
elif h > 40 :
    #calculation of the extra hours worked for
    work_hour = 40
    overtime = h - 40
    normal_pay = work_hour * r
    overtime_gain = overtime * 1.5 * r
    pay = normal_pay + overtime_gain
    
print(pay)