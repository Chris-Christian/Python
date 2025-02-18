N=int(input("Enter N : "))
t1=0
t2=1
next=t1+t2
print("Fibonacci series:", t1, t2, end=" ")  # ✅ Print first two numbers in one line
for i in range(3,N+1):
    print(next, end =" ")  # ✅ Print on the same line
    t1=t2
    t2=next
    next = t1 +t2