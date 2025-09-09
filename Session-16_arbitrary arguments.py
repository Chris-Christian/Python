# *args = allow you to pass non key arguments
# **kwargs = allow you to pass multiple keyword arguments
#            * unpacking operator
#            1. positional 2. DEFAULT 3. keyword 4. arbitrary

def add(*nums):           # *nums collects all extra positional arguments into a tuple
    total=0
    for num in nums:
        total+=num
    return total

print(add(1,4,2,5,7))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Chris", "Christian")
print()

def print_address(**kwargs):   # **kwargs collects all extra keyword arguments into a dictionary
    for key, values in kwargs.items():
        print(f"{key}: {values}")

print_address(apt="Wayne Manor",
              city="Gotham",
              state="fictional")

print()
print()
print()

# both args and kwargs
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "street" in kwargs:
        print(f"{kwargs.get('apt')}, {kwargs.get('street')}")
    else:
        print(f"{kwargs.get('apt')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}")
shipping_label("Chris", "Christian",
                apt="Wayne Manor",
                street="fake street",
                city="Gotham",
                state="fictional")