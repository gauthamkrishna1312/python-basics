def positive():
    print("Positive Integer")


def negative():
    print("Negative Integer")


num = int(input("Enter a positive integer = "))
if num > 0:
    positive()
elif num < 0:
    negative()
else:
    print("Zero")
