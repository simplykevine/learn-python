# Enter Calculation: 5 * 6
# 5 * 6 = 30

# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter calculation').split()
# Convert the string into integers
num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based addition
# print the result

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("use either + - * or / next time ")
