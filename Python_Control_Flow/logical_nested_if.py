#!/usr/local/bin/python3
# This script demonstrates some 


is_student = 'True'
is_employed = 'False'

if is_student and is_employed:
      print("You are a working student.")
if is_student or not is_employed:
      print("You are a student.")
if not is_student and is_employed:
     print("You are employed but not a student.")


# {iii} Nested Loop
message = 'Please enter your age...  '
age = int(input(message))
message += "\nDo you have a driver's license? Yes or No. "
response = (input(message))

if age >= 18 and response == 'Yes':
      print("You are allowed to drive.")
else:
      print("You need a driver's license to drive.")
if age <= 18:
      print('You are not old enough to drive')