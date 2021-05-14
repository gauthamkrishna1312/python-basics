print("Basic arithamatics")

num1 = float(input("Enter First number ="))
num2 = float(input("Second number ="))

print("Enter your deziered operation")
ad = "Addition"
sb = "Subtraction"
ml = "Multiplication"
dv = "Devition"
print(ad,sb,ml,dv)

op = input()
if op == ad:
    redult = num1 + num2
    print(redult)
elif op == sb:
    result = num1 - num2
    print(result)
elif op == ml:
    result = num1*num2
    print(result)
elif op == dv:
    result = num1 / num2
    print(result)
else:print("Invalid input")
