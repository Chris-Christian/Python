isTrue=True
num=int(input("Enter N : "))
if (num<=1):
    isTrue=False
elif(num>1):
        for i in range(2,num):
            if(num%i==0):
                isTrue=False
if(isTrue==False):
     print("Number is not prime")
else:
    print("Number is prime")