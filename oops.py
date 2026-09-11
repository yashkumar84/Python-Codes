#Class  And Object

# class Car:
#     brand = "Toyota"
#     color = "Black"
    

# car1 = Car()
# print(car1.brand)

class Student:
    n = "Yash Tyagi"
    #Constructor
    def __init__(self , name , age , ph):
        self.__name = name
        self.age = age
        self.ph = ph
    #Getters
    def getN(self):
        return self.n
    def getName(self):
        return self.__name
    #Setters
    def setName(self , name):
        self.name = name
        
    
        
st = Student("Himanshu" , 17 , 9089786547)
# print(st.name)
print(st.getName())
st.setName("Himanshu Singh")
print(st.getName())