#!/bin/bash
# This script takes two numbers as arguments. Then use Logical Opertors to check them.

echo Enter your favourite number
read fav_number
echo Enter the precedent number to $fav_number
read number

if ( "$fav_number" -gt 10 )  &&  ( "$number" -gt 10 )
then echo Both numbers are greater than 10
else 
if

fi