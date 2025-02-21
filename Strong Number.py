import math
num=int(input("Enter a number : "))
user_input=num
real_user_input=num
count=0
while(num!=0):
    last_digit=num%10
    num=num//10
    count+=1
num = user_input
flag=count
sum_of_digits=0
while(flag!=0):
    digit=num%10
    sum_of_digits += math.factorial(digit)
    num=num//10
    flag-=1
if(real_user_input==sum_of_digits):
    print(f"{real_user_input} is a Strong number")
else:
    print(f"{real_user_input} is not a Strong number")