name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you?(m) "))
weight = float(input("How much do you?(kg) "))
print("Your name is %s and your age is %s and your height is %f and your weight is %f" % (name, age, height, weight))

# BMI
print("Your BMI is %.2f " % (weight / height ** 2))

