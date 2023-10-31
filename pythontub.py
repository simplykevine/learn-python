# Ask the user to input 2 values and store them in variables num1 num2
num1, num2 = input('Enter 2 numbers: ').split()

# convert the strings into regular numbers Integer
num1 = int(num1)
num2 = int(num2)
# Add the values entered and store in Sum
Sum = num1 + num2
# Subtract values and store in difference
difference = num1 - num2
# Multiply the values and store in product
product = num1 * num2
# Divide the values and store in quotient
quotient = num1 / num2
# use modulus on values to find the remainder
remainder = num1 % num2
# Print the results
print("{} + {} = {}".format(num1, num2, Sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
