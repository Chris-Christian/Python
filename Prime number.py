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

# Optimized code
# isTrue = True
# num = int(input("Enter N: "))

# if num <= 1:
#     isTrue = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):  # ✅ Faster loop (up to √N)
#         if num % i == 0:
#             isTrue = False
#             break  # ✅ Stops unnecessary checks

# if isTrue:
#     print("Number is prime")
# else:
#     print("Number is not prime")
