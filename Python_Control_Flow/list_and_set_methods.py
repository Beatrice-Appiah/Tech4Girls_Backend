#!/usr/local/bin/python3
# This script demonstrates some list methods

#[a] (i)
animals = ['pig', 'fish', 'cow', 'dog', 'sheep', 'giraffe']

# For append()
animals.append('goat')
print(animals)

# For remove()
animals.remove('cow')
print(animals)

# For pop()
print(animals.pop())

# For sort()
animals.sort()
print(animals)

# For reverse()
animals.sort(reverse= True)
print(animals)

# For extend()
animals = ['pig', 'fish', 'cow', 'dog', 'sheep', 'giraffe']
cats = ['tiger', 'lion', 'cheetah', 'bush cat']
cats.extend(animals)
print(cats)

# [a] (ii) Using some Set Methods;

Fav_num = {2, 4, 2, 5, 6, 7, 8, 9}
my_students = {'Afua', 'Adwoa',8, 'Jojo', 'Hawa'}
# For add()
Fav_num.add('222')
print(Fav_num)

# For remove()
Fav_num.remove(9)
print(Fav_num)

# For union()
print(Fav_num.union(my_students))

# For intersection()
print(Fav_num.intersection(my_students))

# For difference()
print(Fav_num.difference(my_students))