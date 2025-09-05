name=input("Enter your full name : ")
result=len(name) #length of string
result=name.find(" ") #index of space
result=name.rfind("s") #last ocuurence of s but index start from beginning
result=name.capitalize #first letter capitalize
result=name.upper()
result=name.lower()
result=name.isdigit() #returns True if all characters are numbers
result=name.isalpha() #returns True if all characters are alphabets
result=name.count("C")
result=name.replace(" ","")

# print(help(str)) other methods of string

print(result)
