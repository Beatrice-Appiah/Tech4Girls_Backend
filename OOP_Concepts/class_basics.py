#!/bin/bash
# this script is to demontrate classes with instance variables and methods in Object Oreinted Progarmming.

# Creating a class Car;
class Car:
# Initilizing the instance variables
    def __init__(self, make,model,year):
        self.make = make
        self.model = model 
        self.year = year

# A method display_info() to print car's details
    def dispaly_info(self):
        return f'The car is a {self.model} from {self.make} that was made in the year {self.year}'

# Creating instances of the Car class with values
car1 = Car('Testla', 'Cyber Truck', 2023)

# Calling and printing methods and variables using instances
print(car1.dispaly_info())
print(car1.model)