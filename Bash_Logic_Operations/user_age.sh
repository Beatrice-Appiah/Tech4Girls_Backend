#!/bin/bash
# THis script asks the user for their age and then displays a message

echo Enter your age
read age

if [ "$age" -le 18 ] then
echo You are a Minor 
else
if [ "$age" -ge 18 ]  &&  [ "$age" -le 64 ] then
echo You are an adult
else
if [ "$age" -eq 65 ]  ||  [ "$age" -gt 65 ] then
echo You are a senior