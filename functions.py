# reusability
# Readability


#Arguments With no return
def add(a , b):
    print(a + b)
    
def add1(a , b , c):
   return a +  b + c


def sub (a , b = 10 ):
    return a - b
    


    
add(10 , 20)
add(140 ,20)

ans = add1(50 , 70 , 10)
print(ans)

print(sub(30 , 15))
print(sub(80))

print(sub(b = 30 , a = 90))  # KeyWord Arguments

#args

def addMultiple(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
    

print(addMultiple(10 , 20 , 30 ,40,  50))

#kwargs

def student(*args , **kwargs):
    print(args)
    print(kwargs)
    
student(10 , 20 , name = "Yash" , job = "Trainer")

#lambda Expression

# def sqaure(x):
#     return x * x

sqaure = lambda x : x * x

print(sqaure(5))

a = int(input("Enter a Number"))
print(a)

a = "10"
print(a)