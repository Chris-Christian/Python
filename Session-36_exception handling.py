# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError (1/0), TypeError (1+"1"), ValueError (int "pizza"))
#             1.try, 2.except, 3.finally

try:
    number=int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")