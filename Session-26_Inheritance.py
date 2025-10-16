# Inheritance=Allows a class to inherit attributes and methods from another class
#             Helps with code resuability and extensibility
#             class child(parent)

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Mouse(Animal):
    def speak(self):
        print("SQueek")

dog=Dog("Bob")
cat=Cat("Tom")
mouse=Mouse("Jerry")

dog.speak()
cat.eat()
mouse.sleep()