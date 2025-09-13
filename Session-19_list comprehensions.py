# List comprehensions = a concise way to create lists in Python
#                          compact and easier to read than traditional loops
#                          [expression for value in iterable if condition]

doubles=[x*2 for x in range(1,11)]
print(doubles)

fruits=["apple","banana","mango","orange"]
fruits=[fruit[0] for fruit in fruits]       #returns 1st characters of fruits
print(fruits)

nums=[-9,-4,-1,2,3,4,5]
positive_nums=[num for num in nums if num>0]
negative_nums=[num for num in nums if num<0]
even_nums=[num for num in nums if num%2==0]
odd_nums=[num for num in nums if num%2==1]
print(positive_nums)
print(negative_nums)
print(even_nums)

print(odd_nums)
