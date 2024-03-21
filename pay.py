def computepay() :
    if h <= 40 :
        pay = h * r
        print(pay)
    else :
        work_hour = 40
        extra_hour = h - 40
        extra_pay = extra_hour * 1.5 * r
        usual_pay = work_hour * r
        gross_pay = usual_pay + extra_pay

    return gross_pay

hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')

try :
    h = float(hrs)
    r = float(rate)
except : 
    print("Error, please enter numeric input")
    quit()

p = computepay()
print("Pay", p)