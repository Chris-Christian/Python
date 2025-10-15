# class variables = shared among all instances of the class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    class_year=2027
    num_of_students=0

    def __init__(self,name,age):
        self.name=name
        self.age=age                        #This constructor is called everytime we create an object 
        Student.num_of_students+=1

student1=Student("Rahul",20)
student2=Student("Rohan",21)
student3=Student("Karan",20)
student4=Student("Ramesh",19)

print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)