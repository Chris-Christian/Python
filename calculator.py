# input() always returns a string!
# To convert it to a number, use int() or float()
# fav_number = int(input("Enter your favorite number: "))
# → Normal division (float result)
# → Floor division (integer result)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /,**,%")
operation = input("Enter operation: ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
     result = print("Cannot divide by zero")
    else:
     result = num1 / num2
elif operation == "**":
    result = num1 ** num2     
elif operation == "%": 
   if num2 == 0:
    result = print("Cannot divide by zero")
   else:
       result = num1 % num2    
else:
    result = "Invalid operation"

print(f"Result: {result}")
