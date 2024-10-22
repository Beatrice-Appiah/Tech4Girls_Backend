#!/bin/bash
# This script takes 'n' then calculates the sum of all numbers from 1 to 'n'

echo Enter any digit
read n
sum=0

for (( i=1; i<=n; i++ ))
do
sum=$((sum+i))
done
echo The sum of numbers from 1 to $n is: $sum
