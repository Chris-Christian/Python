# keyword arguments= an argument preceded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. positional 2. DEFAULT 3. keyword 4. arbitrary

print("1","2","3",sep="-")
for i in range(1,6):
    print(i, end=" ")
# Here end and sep are keyword arguments of print function

def get_phone(country_code, first, last):
    return f"{country_code}-{first}-{last}"
phone_num=get_phone(country_code="+91",first=98765,last=43210)
print(phone_num)