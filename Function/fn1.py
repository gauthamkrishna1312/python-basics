def hey(*values):
    print("First " + values[0] + "\nsecond " + values[1])


hey("Hello", "World")


# Globel and local variable

def lcl():
    a = 20 #Local variable which is inside the function lcl
    print(a)

lcl()
a = 10  # Globel variable which is out side of the function lcl
print(a)
