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
    sum_of_digits += digit ** count
    num=num//10
    flag-=1
if(real_user_input==sum_of_digits):
    print(f"{real_user_input} is an Armstrong number")
else:
    print(f"{real_user_input} is not an Armstrong number")



#Range of armstrong numbers from 1 to N

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
        sum_of_digits += digit ** count
        i=i//10
        flag-=1

    if(real_user_input==sum_of_digits):
        print(f"{real_user_input}",end=" ")
