#!/usr/local/bin/python3
# This script demonstrates methods of indexing

age = int(input("Enter your age...."))

if age < 18:
    print('You are a minor.')
elif age in range(18,64):
    print('You are an adult.')
else:
    print('You are a senior.')
