print("Calculator Using the Python")
print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")
option  = int(input("What do you want to do? "))
if option in [1,2,3,4]:
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        if num2 == 0:
            result = num1
        else:
            result = num1 / num2
else:
    print("Invalid operation")
print("The result is",result)

