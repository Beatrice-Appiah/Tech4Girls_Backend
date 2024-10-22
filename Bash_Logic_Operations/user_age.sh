#!/bin/bash
# THis script asks the user for their age and then displays a message

echo Enter your age
read age

if [ "$age" -lt 18 ] then
echo You are a Minor 
elif [ "$age" -ge 18 ]  &&  [ "$age" -lt 65 ];
then
echo You are an adult
else
echo You are a senior
fi