#!/bin/bash
# This script takes two numbers as arguments. Then use Logical Opertors to check them.

Number1=$1
Number2=$2

if [ "$Number1" -gt 10 ]  &&  [ "$Number2" -gt 10 ]
then echo "Both numbers are greater than 10"
elif [ $Number1 -gt 10 ] || [ $Number2 -gt 10 ] 
then 
echo "At least number is greater then 10"
else echo "Neither number is greater than 10"
fi