N=int(input("Enter N : "))
for i in range(1,N+1):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(i==sum):
        print(i)
