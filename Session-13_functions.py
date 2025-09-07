# function= a block of reusable code to perform a specific task
#           place a () after the function name to invoke it

def invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ₹{amount:.2f} is due: {due_date}")

invoice("Chris", 5000, "02/07/2024")

# return= end a function and send a result back to the caller

def create_name(first, last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

fullname= create_name("Chris", "Christian")
print(fullname)