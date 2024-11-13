# Question 1: Division Calculator

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
try:
    result = numerator / denominator
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("The result is:", result)