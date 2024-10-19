#!/bin/bash
# This script takes a number as an argument and checks if it is odd or even.

echo Enter your favourite number
read number

if (( $number == "even" ))
then 
echo The number $number is even
else
echo The number $number is odd 
fi