def check(number):
    if number > 0:
        print("Positive Integer")
    elif number == 0:
        print("Zero")
    else:
        print("Negative Integer")


check(float(input("Enter a number = ")))
value = int(input("Now enter an integer = "))
check(value)
