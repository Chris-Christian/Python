# object=a "bundle" of related attributes(variables) and methods(functions)
#        Ex. phone, cup, book 
#        You need a class to create many objects

# class= (blueprint) used to design the structure and layout of an object

from car import car

car1=car("Mustang",2024,"red",False)
car2=car("BMW",2025,"Black",True)
#print(car1) #print memory address of this car object
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car2.stop()
car1.describe()