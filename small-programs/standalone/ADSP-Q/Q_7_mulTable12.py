# Write a program that prints a multiplication table for numbers up to 12.

for i in range(1, 13):
    print(f"Table of {i}: ")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
