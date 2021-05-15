def sample(name, age):
    print(name, age)


sample("Gautham", "19")
sample(age=19.7, name="Gautham Krishna P")  # Key word argument

#Default argument
def sample1(name, age=19):
    print(name, age)


sample(name="Gautham",age=20)
