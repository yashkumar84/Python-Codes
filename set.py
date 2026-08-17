number = {1 , 2 , 3 , 4 , 5 , 6}

print(number)

list = [1  , 2 , 2 , 3 , 3 , 4 , 9]
unique = set(list)
print(unique)

print(9 in number)

#Union
print(number | unique)

#Intersection
print(number & unique)

#Difference

print( number - unique)

# a - b |  b - a
#Symmetric 
print(number ^ unique)