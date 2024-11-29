#!/bin/bash
# this script is to demontrate inheritance and the use of the super() method in Object Oreinted Progarmming.

# The class Employee is created;
class Employee:
# Initializing the instance variables
    def __init__(self, name,position):
        self.name = name
        self. position = position

# A method to display the employee's details 
    def get_details(self):
       return f"\nYou are {self.name} and you hold the position of {self.position}. "

# The child class(Manager) is created;
class Manager (Employee):
# Initializing the instance variables using supeer() and adding a new attribute for the child class
    def __init__(self, name, position, department):
        super().__init__(name,position)
        self.department =  department

# A method to display the employee's details including the new attribute fom the child class
    def get_details(self):
        super().get_details()
        return f"\nYou are {self.name} and you hold the position of {self.position} and you are in {self.department}"

# Instances for class Employee and child class Manager
emp1 = Employee("Beatrice", "Supervisor")
emp2 = Manager("Akua", "Assitant Manager", "IT Department")

# Demonstration to print instances of both classes by calling get_details() for each.
print(emp1.get_details())
print(emp2.get_details())  