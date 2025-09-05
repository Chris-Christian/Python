import math
N=int(input("Enter N : "))
for i in range(1,N+1):
    user_input=i
    real_user_input=i
    count=0
    while(i!=0):
        last_digit=i%10
        i=i//10
        count+=1
    i = user_input
    flag=count
    sum_of_digits=0
    while(flag!=0):
        digit=i%10
        sum_of_digits += math.factorial(digit)
        i=i//10
        flag-=1

    if(real_user_input==sum_of_digits):
        print(f"{real_user_input}",end=" ")
