#!/bin/bash
# This script takes three numbers as arguments and calculate

echo Enter any number
read num_1
echo Enter any 2nd number
read num_2
echo Enter any 3rd number
read num_3
# Addition of numbers
a=$num_1
b=$num_2
Sum=$((a+b))
echo The sum of $a and $b is: $Sum
# Mulitiplication
c=$Sum
d=$num_3
Multiplication=$((c*d))
echo Multiplying the $c by $d gives: $Multiplication

