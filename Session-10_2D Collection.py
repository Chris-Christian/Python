fruits=["apple","Mango","Banana"]
vegetables=["Potato","Eggplant","Carrots"]
Meat=["Chicken","Fish","Beef"]

Groceries=[fruits,vegetables,Meat]

# Groceries=[["apple","Mango","Banana"],
#            ["Potato","Eggplant","Carrots"],       #We can also initialize like this
#            ["Chicken","Fish","Beef"]]

# print(Groceries[0]) #Print whole 1st row
print(Groceries[0][1]) #print mango

# for i in Groceries:
#     print(i)            #Print whole matrix

for collection in Groceries:
    for food in collection:
        print(food,end=" ")
    print()