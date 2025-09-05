temperature=float(input("Enter Temperature : "))
unit=input("Enter unit of your input (celsius or fahrenheit): ")
if unit=="celsius":
    Celsius=temperature
    Fahrenheit=(Celsius*9/5)+32
    print(f"Temperature in Fahrenheit is {round(Fahrenheit,1)}")
elif unit=="fahrenheit":
    Fahrenheit=temperature
    Celsius=(Fahrenheit-32)*5/9
    print(f"Temperature in Celsius is {round(Celsius,1)}")
else:
    print(f"Entered unit '{unit}' is invalid")
