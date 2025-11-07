# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("*You add sprinkles*")
        func(*args,**kwargs)    
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("*You add fudge*")
        func(*args,**kwargs)    
    return wrapper

@add_sprinkles                                 #decorated_function = add_sprinkles(get_ice_cream)
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("Vanilla")

# wrapper()	        The new function that adds extra behavior around the original function
# *args, **kwargs	Makes the wrapper work with any function signature
# return wrapper	Returns the new modified version that replaces the original function