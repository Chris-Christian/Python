num = int(input("Enter a number: "))
print(f"Prime factors of {num} are:", end=" ")
factor = 2
while num > 1:
    if num % factor == 0:
        print(factor, end=" ")
        num = num // factor
    else:
        factor += 1

# Divide Repeatedly by the Same Factor:
# If a number is divisible by 2, the program keeps dividing the number by 2 until it’s no longer divisible. This ensures that all occurrences of the prime factor 2 are extracted.
# For example, if the number is 24:
# 24 ÷ 2 = 12 → factor 2
# 12 ÷ 2 = 6 → factor 2
# 6 ÷ 2 = 3 → factor 2
# Now, 3 is not divisible by 2, so the program moves to the next number.