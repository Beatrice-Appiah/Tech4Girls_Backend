# Question 2: Dictionary Lookup

while True:
    try:
        data = {"name": "Alice", "age": 25, "country": "Wonderland"}
        key = input("Enter the key you want to look up: ")
        print("Value:", data[key])
        break
    except KeyError:
        print("This key does not exist in the data dictonary")
