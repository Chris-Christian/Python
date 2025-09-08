# default arguments= a default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible 
#                    1. positional 2. DEFAULT 3. keyword 4. arbitrary

def net_price(list_price,discount=0,tax=0.05):
    return list_price*(1-discount)*(1+tax)
print(net_price(5000))

import time

def count(end, start=0):
    for i in range(start, end+1):
        print(i)
        time.sleep(1)
    print("DONE!")

count(10)