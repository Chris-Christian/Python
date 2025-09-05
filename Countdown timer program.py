import time
my_time=int(input("Enter the time in seconds: "))

# for i in range(0, my_time):    #0 1 2 time's up
#     print(i)
#     time.sleep(1)

for i in range(my_time,0,-1):    
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIMES' UP!")