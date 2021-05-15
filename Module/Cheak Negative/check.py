print("Hello")


def check(num):
    if num > 0:
        print("Entered number is positive\n")
    elif num == 0:
        print("Entered value is Zero")
    else:
        print("Entered number is negative")


check(float(input("Enter a number\n")))
