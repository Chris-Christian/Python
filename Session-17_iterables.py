numbers=[1,2,3,4]
for num in reversed(numbers):
    print(num)
print()
my_dictionary={"A":1,"B":2}
for key in my_dictionary:
    print(key)
for value in my_dictionary.values():
    print(value)
for key, value in my_dictionary.items():
    print(f"{key}:{value}")