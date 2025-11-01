# static methods = A method that belong to a class rather than any object from the class (instance)
#                  Usually used for general utility functions
                    
# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name=name
        self.position=position
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions=["Manager","Cashier","Cook","Janitor"]   #no self in static methods
        return position in valid_positions

employee1=Employee("Tom","Cook")
employee2=Employee("Jerry","Cashier")
employee3=Employee("Spike","Manager")
employee4=Employee("Butch","Janitor")

print(Employee.is_valid_position("Rocket Scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())