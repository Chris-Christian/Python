# dicrionary : a collection of {key:value} pairs
# Ordered and changeable (No duplicates)

capitals={"India":"New Delhi",
          "USA":"Washington D.C",
          "Russia":"Moscow",
          "China":"Beijing"}

#print(dir(capitals)) attributes and methods of dictionaries
# print(help(capitals))

print(capitals.get("India")) #print value(capital)
if (capitals.get("Japan")):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany":"Berlin"})
capitals.update({"Germany":"random"})
capitals.pop("Germany")
capitals.popitem() #pop last
# capitals.clear()
print(capitals)

keys=capitals.keys()
# print(keys)
for key in keys:
    print(key)

values=capitals.values()
# print(values)
for value in values:
    print(value)

items=capitals.items()
#print(items)
for key,value in items:
    print(f"{key} : {value}")