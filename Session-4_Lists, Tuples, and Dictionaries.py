# Lists []- A list is an ordered, mutable collection that can store different data types.
# Tuples ()- A tuple is similar to a list but immutable (cannot be modified after creation).
# Dictionaries {} - A dictionary stores key-value pairs, allowing fast lookups.
# A list of numbers
numbers = [10, 20, 30, 40, 50]
print(numbers)

print(numbers[0])  # First element
print(numbers[-1])  # Last element

# A list with mixed data types
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)
numbers.append(60)  # Add an element
print(numbers)

numbers.remove(30)  # Remove an element
print(numbers)

numbers[2] = 100  # Modify an element
print(numbers)


#Dictonaries
student = {
    "name": "Chris",
    "age": 20,
    "course": "Computer Engineering"
}
print(student)

print(student["name"])  # Output: Chris

student["city"] = "New York"  # Adding a key-value pair
student["age"] = 21  # Modifying an existing value
print(student)

del student["city"]
print(student)

print("=====================================================================================================")

number=[]
for i in range(5):
    user_input=int(input("Enter any number : "))
    number.append(user_input)
print(number)    

tuple_one=tuple(number)
print(tuple_one)

square={}
for i in number:
    square[i]=i**2             #square = {num: num**2 for num in number}
print(square)
