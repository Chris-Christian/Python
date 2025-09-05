price1=3.124324
price2=-948.35
price3=12.34

print(f"Price 1 is {price1:.2f}") #3.12
print(f"Price 2 is {price2:.1f}") #-984.4
print(f"Price 3 is {price3:}") #12.34

print(f"Price 1 is {price1:>10}") #move right
print(f"Price 2 is {price2:<10}") 
print(f"Price 3 is {price3:^10}") #move center

print(f"Price 1 is {price1:+}") #positive number preceeded with positive sign
print(f"Price 2 is {price2:+}")  #negative number preceeded with negative sign
print(f"Price 3 is {price3:+}") 

print(f"Price 1 is {price1:,.2f}") #thousand separator with decimal precision 
print(f"Price 2 is {price2:,}") 
print(f"Price 3 is {price3:,}") 
