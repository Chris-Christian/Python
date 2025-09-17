# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB order) Local -> Enclosed -> Global -> Built-in

x=9                 #global

def func():
    a=2             #a is local variable
    print(a)
func()

def func1():
    # x=1             #enclosed
    def func2():
        # x=4       #local
        print(x)
    func2()
func1()


from math import e

def func3():
    print(e)        #Built-in
func3()