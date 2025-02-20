num=int(input("Enter a number : "))
user_input=num
reverse=0
while(num!=0) :
    last_digit=num%10
    reverse=reverse*10+last_digit
    num=num//10
print(f"Reversed number is {reverse}")
if(reverse==user_input):
    print("It's Palindrome")    
else:
    print("It's not a Palindrome")