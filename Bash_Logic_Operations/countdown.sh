#!/bin/bash
# This script takes a number as input and counts down from that number

echo Enter any number of your choice
read number

while [ $number -ge 1 ]
do 
echo $number 
number=$((number-1))

if (( "$number" == 0 )); then
break
echo Coundown complete!
fi
done