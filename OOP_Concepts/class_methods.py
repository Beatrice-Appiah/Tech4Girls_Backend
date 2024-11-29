#!/bin/bash
# this script is to demontrate class variables, class methods and static method in Object Oreinted Progarmming.

# The class BankAccount is created;
class BankAccount:
    # assigning a class variable "bank_name" and initializing it
    bank_name = "Tech4Girls Bank"
# Initializing the instance variables
    def __init__(self, account_holder):
        self. balance = 0
        self.account_holder = account_holder
        
#A method deposit(amount) to add money to the account.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'\n Your account has been updated. Your new balance is {self.balance}'
        else:
            print('\n Invalid amount. Please try again')
# A method withdraw(amount) to deduct money, ensuring the balance doesn’t go negative.
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            return f'\n Your account has been debited with {amount}'
        else:
            print(f'\n Your balance is insufficient to proceed')

# A static method bank_policy() that prints a generic policy message.
    @staticmethod
    def bank_policy():
        return f'\n Bank Policy: Terms and policies apply to every package !!!'

# A class method get_bank_name() to return the bank name.
    @classmethod
    def get_bank_name(cls):
        return f'\n This is {cls.bank_name} '

# Values for instance variables using instances 
cus1 = BankAccount('Beatrice')
cus2 = BankAccount('Samuella')

# Values using instances for method deposit()
cus1.deposit(100)
cus2.deposit(500)

# Values using instances for method withdraw()
cus1.withdraw(10000)
cus2.withdraw(100)

# Calling and printing all three methods
BankAccount.bank_policy()
print(BankAccount.bank_policy())
print(BankAccount.get_bank_name())