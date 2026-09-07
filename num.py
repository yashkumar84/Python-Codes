import numpy as np


number = np.array([1 , 2 , 3, 4, 5, 6])

number = number * 5

print(type(number))
print(number)

num = np.arange(3 , 16 , 2)
print(num)

zeroes = np.zeros(10)
print(zeroes)

ones = np.ones(8) * 3
print(ones)

mean = np.mean([1 , 2 , 3, 4 ,5 , 6 ])
print(mean)

median = np.median([1 ,2 , 3, 4, 5 , 6])
print(median)

std = np.std([1 , 2 , 3, 4 , 5, 6])
print(std)

var = np.var([1 ,2 ,3 ,4 ,5 ,6])
print(var)

min = np.min([1 , 2, 3, 4,5 ,6 ,7 ])
print(min)

max = np.max([1 , 2, 3, 4,5 ,6 ,7 ])
print(max)


sum = np.sum([1 , 2, 3, 4,5 ,6 ,7 ])
print(sum)

part = np.linspace(2 , 10 , 5)
print(part)

twod = np.array([[1 , 2, 3] , [4 ,5 ,6] , [7 ,8 ,9 ]])
print(twod)

#Slicing 

