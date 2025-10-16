# multiple inheritance=inherit from more than one parent class
#                      C(A,B)
# multilevel inheritance=inherit from a parent which inherits from another parent
#                        C(B)<-B(A)<-A

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
class Rabbit(prey):
    pass
class Hawk(predator):
    pass
class Fish(prey, predator):
    pass

rabbit=Rabbit("Bunny")
hawk=Hawk("Raptor")
fish=Fish("Megalodon")

hawk.hunt()
rabbit.sleep()
fish.flee()
fish.hunt()