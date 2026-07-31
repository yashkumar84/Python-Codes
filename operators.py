#Arithmetic Operators

# + , - , / , * , // , % , **

a = 8
b = 4
print(a + b) # 12
print(a - b)   #4
print(a * b)  #32
print(a / b) #2.0 -- Division 
print(a // b) #2 -- Floor Division 
print(a % b) #0 -- Modulus Operator - Remainder 
print(2 ** 3) #8 -- Power Operator

#Conditional Operators

print(10 < 20)
print(10 > 20)
print(10 == 10)
print(10 != 10)
print( 10 <=10)
print(10 >= 20)

#Logical Operators
#and , or , not
print(10 < 20 and 30 < 30 and 30 < 40)
print(10 < 20 or 30 < 30 or 30 < 40)
print(10 < 20 and 30 < 30 or 30 < 40)
print(10 < 20 or 30 < 30 and 30 < 40)
print(not(10 < 20 or 30 < 30 and 30 < 40))
print(not True)

#Assignment Operator

b = 90
b += 2 #b = b + 2
print(b)
b -= 2 #b = b - 2
print(b)
b *= 2 # b = b * 2
print(b)
# b /= 2 # b = b / 2
# print(b)
b //= 2 # b = b // 2
print(b)
d = 2
d **= 2
print(d) 
b %= 2
print(b)

# Membership Operator

print('na' in "narrow")
print('n' not in "narrow")

#Identity Operator
a = b

print(a is b)
print(a is not b)
c = 10
d =10
print(c is d)

# Bitwise Operator

# | , & , ^ , << , >>

print(12 & 11)
print(12 | 11)
print(12 ^ 11)
print(5 << 1)
print(5 >> 1)