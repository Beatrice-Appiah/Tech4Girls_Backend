# Question 4: List Index Access

items = ["apple", "banana", "cherry"]

while True:
    try:
        index = int(input("Enter the index of the item you want to access: "))
        print("You selected:", items[index])

        break
    except IndexError:
     print("This index does not exist")
    