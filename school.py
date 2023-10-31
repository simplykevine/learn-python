# If age is 5 go to Kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater than 17 say go to college
# Try to complete with 10 or less lines

# Ask for age
age = eval(input("Enter age: "))

# Handle if age < 5
if age < 5:
    print("Too young for school")

# Special output just for age 5
elif age == 5:
    print("Go to kindergarten")

# Since a number is the result for ages 6 - 17 we can check them all with 1 condition
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
# Handle everyone else
else:
    print("go to college")
