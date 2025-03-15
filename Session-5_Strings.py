# Some Common String Functions:
# len(s) → Returns the length of the string.
# s.upper() → Converts to uppercase.
# s.lower() → Converts to lowercase.
# s.replace("old", "new") → Replaces part of the string.
# s.count("a") → Counts occurrences of a character.
# s.find("word") → Finds the index of a substring.

s=input("Enter a string : ")
print(len(s))
print(s.upper())
print(s.lower())
print(s[0])
print(s[-1])

#Slicing:String slicing allows you to extract a part (or "slice") of a string
#string[start:end]           Extracts characters from index 'start' to 'end-1'
s1=input("Enter a string : ")
print(s1[0:3])
print(s1[-3:])
print(s1[1:-1])

# string manipulation techniques like:
# ✅ Concatenation (+)
# ✅ Repetition (*)
# ✅ Membership (in, not in)

string1=input("Enter a string : ")
string2=input("Enter a string : ")
print(string1+" "+string2)
print(string1*3)
print(string2 in string1)     #Check if string2 exist in string1 then return True or False
