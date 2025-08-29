menu={"soda":20,
      "popcorn":60,
      "pizza":150,
      "fries":60}
cart=[]
total=0

print("-------------MENU-------------")
for key, value in menu.items():
    print(f"{key:20}{value} Rs")
print("------------------------------")    
print()

while True:
    item=input("Select your item (q to quit): ").lower()
    if item=="q":
        break
    elif menu.get(item) is not None:
        cart.append(item)

print()
print("----------YOUR CART----------")
for item in cart:
    total += menu[item]
    print(f"{item:20}", end=" ")
print()
print()
print("========== RECEIPT ==========")
print(f"{"Item":20}Price")
print("-----------------------------")
for item in cart:
    print(f"{item:20}{menu[item]} Rs")
print("-----------------------------")
print(f"{"Total Bill":20}{total} Rs")
print("=============================")
