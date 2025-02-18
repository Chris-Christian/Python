# for i in range(1, 6):
#     print(f"Hello, this is message {i}")

# count = 1
# while count <= 5:
#     print(f"Count: {count}")
#     count += 1

N = int(input("Enter value for N : "))
for i in range (1,N+1):     # Include N in the range
    if(i % 2 == 0):
        print(f"{i}")

# 💡Optimization
# You can start the loop from 2 (first even number) and step by 2 to skip checking odd numbers:

# N = int(input("Enter value for N: "))  
# for i in range(2, N + 1, 2):  # ✅ Start from 2, step by 2
#     print(i)

