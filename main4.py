opration = int(input("1 for addtion 2 for subtraction 3 for divstion 4 for mutplcation"))
a = int(input("what do you want the first number to be"))
b = int(input("what do you wnat the second number to be"))
addtion = a + b
divsion = a / b
mutplcation = a * b
subtraction = a - b
if opration == 1:
    print(addtion)
if opration == 3:
    print(divsion)
if opration == 2:
    print(subtraction)
if opration == 4:
    print(mutplcation)