from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self , *args):
        pass

    


class Dog(Animal):
    def sound(self):
        print("The Dog is barking")



def print_sound(obj):
    obj.sound()

obj = Dog()
# obj.sound()
print_sound(obj)
print(ord('A'))