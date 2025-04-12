# collection = single variable used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits=["apple","orange","banana","coconut"]

# print(dir(fruits))
# print(help(fruits))

print(len(fruits))  #length of list
print("pineapple" in fruits)   #Boolean
fruits[0]="Pineapple"
fruits.append("Mango")
fruits.remove("Mango")
fruits.insert(2, "Mango")
fruits.sort()
fruits.reverse()
# fruits.clear()   #clear list
print(fruits.index("Mango"))
print(fruits.count("banana"))
print(fruits[0:2])
for i in fruits:
    print(i)



#SET
fruits={"apple","orange","banana","coconut"}
#we can't use inedxing or change value but we can add or remove
#no duplicates
fruits.pop()  #delete first element but it's random


#TUPLE
#faster than list
new_tuple=("a","b","c","d")
print(len(new_tuple))
print("d" in new_tuple)
print(new_tuple.index("c"))
print(new_tuple.count("d"))