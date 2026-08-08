yash = [1 ,7 ,3 ,4 ,5, 6 , 2]
print(len(yash))

# for i in yash:
#     print(i)


print(sum(yash))
print(min(yash))
print(max(yash))
print(sorted(yash))
yash.reverse()
print(yash)
yash.append(10)
print(yash)
yash.insert(2 , 30)
print(yash)
yash.pop()
print(yash)
yash.remove(2)
print(yash)
yash.pop(3)
print(yash)
yash1 = yash
print(yash1)
yash1 = yash.copy()
yash.extend([40 , 50 ,60 ,70])
print(yash)
print(yash.index(40))
print(yash[::-1])
print(yash[0 : 4])
print(yash[6 : 3 : -1])


