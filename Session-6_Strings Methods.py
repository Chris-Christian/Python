s = "  Hello  "
print(s.strip())   # "Hello" (removes spaces from both sides)
print(s.lstrip())  # "Hello  " (removes left spaces)
print(s.rstrip())  # "  Hello" (removes right spaces)

s = "Hello World"
print(s.replace("World", "Python"))  # "Hello Python"

s = "apple,banana,grape"
print(s.split(","))  #string to list ['apple', 'banana', 'grape']

words = ['Python', 'is', 'awesome']
print(" ".join(words))  #list to string "Python is awesome"

user=input("Enter a string : ")
print(user.strip())
print(user.replace("bad","good"))
wordss=user.split(" ")
print(words)
print("-".join(wordss))