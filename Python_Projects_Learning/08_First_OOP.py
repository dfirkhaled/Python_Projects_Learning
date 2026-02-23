# Created in 2/24/2026 at 1:47 AM


from abc import ABC, abstractmethod



class Pet(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def say_hello(self):
        pass


class Cat(Pet):
    def say_hello(self):
        return f"Hello, my name is: {self.name} and i am {self.age} years old"

class Dog(Pet):
    def say_hello(self):
        return f"Hello, my name is: {self.name} and i am {self.age} years old"
    

my_cat = Cat("Rexy", 1.5)
my_dog = Dog("Rex", 3)
pets = [my_cat, my_dog]
for pet in pets:
    print(f"{pet.say_hello()}")