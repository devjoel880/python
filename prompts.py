largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        num = int(num)
        if largest is None:
            largest = num
        if num > largest:
            largest = num
        if smallest is None:
            smallest = num
        if num < smallest:
            smallest = num
    except:
        print("Invalid input")

if largest is not None:
    print("Maximum is", largest)
if smallest is not None:
    print("Minimum is", smallest)
