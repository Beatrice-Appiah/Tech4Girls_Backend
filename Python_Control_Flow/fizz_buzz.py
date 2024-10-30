#!/usr/local/bin/python3
# This script demonstrates some the fizzbuzz challenge

#loops from numbers 1 to 50
for i in range(1,51):

#Prints "Fizz" if % 3 
    if(i % 3 == 0):
         print('Fizz')
#Prints "Buzz" if number % 5;
    if(i % 5 == 0):
          print('Buzz')
#Prints "FizzBuzz" if the nunmber is divisible by both 3 and 5
    if(i % 5 and i % 3 == 0):
         print('FizzBuzz') 
#Else print (i)
    else:
         print(i)