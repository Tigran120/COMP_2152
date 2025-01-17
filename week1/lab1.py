# Questions 01 Week 01
# First Name: Tigran
# Last Name: Khachaturyan

# Defining Variables
numbers = [1, 4, 7, 9]

# Order of Operations
a, b, c, d = 1, 2, 3, 4
e1 = (a * c) - (b / d)

# Fully-Bracketed Version:
e2 = ((a - ((b ** c) // d)) + (a % c))

# Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))  # Formatting with 3 decimal places

# Common Functions
userAge = int(input("Please enter your age: "))
userAge += 22
print("Now showing the shop items filtered by age:" + userAge)
