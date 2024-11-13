# Question 3: Integer Conversion
while True:
    try:
        user_input = input("Enter a number: ")
        converted_number = int(user_input)
        print("The number you entered is:", converted_number)
        break
    except ValueError:
        print("Please enter a number")
