#While Loop

name=input("Enter your name: ")
while name == "":
    print("You didn't enter any name")
    name=input("Enter your name: ")
print(f"Hello {name}")

food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")
print("Bye")

#for loop

for i in reversed(range(1,11)):     #print 10 to 1
    print(i)

for i in (range(1,11,2)):     #print 1,3,5,7,9
    print(i)

example="hello there!"    #print hello there!
for i in example:
    print(i,end="")
