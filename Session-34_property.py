# @property = Decorator used to define a method as a property(it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you better, setter and deleter mode

class Rectangle:
    def __init__(self,width,length):
        self._width=width                   #_width, _length - private attributes
        self._length=length

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def length(self):
        return f"{self._length:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("Width must be greater than zero")
    @length.setter
    def length(self, new_length):
        if new_length>0:
            self._length=new_length
        else:
            print("Length must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")        
    @length.deleter
    def length(self):
        del self._length
        print("Length has been deleted")  

rectangle=Rectangle(3,4)

rectangle.width=5
rectangle.length=6

print(rectangle.width)
print(rectangle.length)

del rectangle.width
del rectangle.length