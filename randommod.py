import numpy as np

number = np.random.randint(1 , 10000, 4)

print(number)
a = [1 ,2 ,3 ,4 , 5]

print(np.prod(a))
print(np.cumsum(a))
print(np.argmax(a))

print(np.random.choice(a , 3 , replace=False))

print(np.random.uniform(10 , 20 , 3))
np.random.shuffle(a)
print(a)


#randn


#Vectorization 
#Broadcasting 

