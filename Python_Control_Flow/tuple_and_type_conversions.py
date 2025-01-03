#!/usr/local/bin/python3
# This script demonstrates methods of indexing and conversion of data types


tuple_1 = ('Afua', 'Adwoa', 'Ama', 'Jojo', 'Hawa')

# Index for the first element
first_element = tuple_1[0]
print("First element:", first_element)

# Index for the second element
second_element = tuple_1[-1]
print("Second element", second_element)

# The use of count on the tuple
count = tuple_1.count('Adwoa')
print(count)

# The use of index on the tuple
index = tuple_1.index('Jojo')
print(index)

# Conversion of an integer to a float 
g = 288
i = float(g)
print(i)

# Conversion of a float to an integer
a = 5.78
b = int(a)                                                                                
print(b)

# Conversion of a string representinga number to an integer
d = '345'
e = int(d)
print(e)

incorrect = ('Hello', 'Beatrice', 'Appiah!', 'Welcome', 'to', 'Bash', 'Scripting.')
correct = ' '.join(incorrect)
print(correct)