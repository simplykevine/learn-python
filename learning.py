# problem : Receive miles and convert to kilometers
miles = input('Enter miles ')

# Convert string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934

# Print result using format()
print(" {} miles equals {} kilometers".format(miles, kilometers))
