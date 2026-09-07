import numpy as np

twod = np.array([[1 ,2 ,3 ], [4 ,5, 6] ])
twod1 = np.array([[3 , 4] , [1 ,2 ] , [5 , 6]])

print(twod@twod1)

arr = np.array([1, 2, 3, 4, 5, 6])
arr1 = np.array([1, 2, 3, 4, 5, 6 , 7 , 8, 9 , 10 , 11 , 12])

# arr2 = arr + arr1
# print(arr2)

# print(arr * arr1)

print(twod.sum(axis=1))

print(arr > 4)
print(arr[arr > 4])

# print(arr1)

arr1 = arr1.reshape(3 , 4)

# arr1 = arr1.reshape(-1)
arr1 = arr1.ravel()

print(arr1)


unsorted = np.array([1 ,  9 , 6 ,3 , 8 , 2, 7])
sor = np.argsort(unsorted)
print(sor)
b = [3 , 5 , 1, 7, 2 ]
b.sort(reverse=True)
print(b)
