# Polymorphism=Greek words that means to "have many forms or faces"
#              Poly=many
#              Morphe=Form

#              Two ways to achieve Polymorphism 
#              1. Inheritance=An object could be treated of the same type as a parent class
#              2. "Duck typing"=Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side=side
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height

class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping=topping

shapes=[Circle(4),Square(5),Triangle(6,7),Pizza("Pepperoni",15)]   

for shape in shapes:

    print(f"{shape.area()}cm²")

# ABC → A base class you inherit from to make your class abstract.
# @abstractmethod → A decorator that marks a method as abstract, meaning subclasses must override (implement) it.
# Shape is an abstract class — you can’t create an object of it directly (Shape() would cause an error).
# Any class that inherits from Shape must implement the area() method.
# So if you forget to write def area(self): in a subclass (like Circle, Square, or Triangle), Python will raise an error — forcing you to define it.
