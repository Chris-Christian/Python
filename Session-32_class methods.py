# class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

class Student:
    count=0
    Total_gpa=0
    
    def __init__(self, name, gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.Total_gpa+=gpa
    
    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"Average gpa: {cls.Total_gpa/cls.count:.2f}"

student1=Student("Mr. A",8.14)
student2=Student("Mr. B",7.78)
student3=Student("Mr. C",8.55)
print(Student.get_count())
print(Student.get_average_gpa())