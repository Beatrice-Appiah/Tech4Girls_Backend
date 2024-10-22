#!/bin/bash
#this script takes two numbers as input and use comparison operators to check which number is greater or equal.

echo Enter any number
read num_1
echo Enter any number again
read num_2

if (( "$num_1" -gt "$num_2" ))
then
echo $num_1
else 
echo $num_2
else if (( "$num_1" = "$num_2" )) then 
echo $num_1 $num_2
fi