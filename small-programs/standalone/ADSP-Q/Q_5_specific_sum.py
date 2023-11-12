# Modify the previous program such that only multiples of three or five are considered in the sum,
# e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

# 5*3 = 15...so why not?
def add_15_stuff(n: int) -> int:
    sumNow = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            sumNow += i
    return sumNow


number = int(input("Enter value of n: "))
print(
    f"The sum till {number}, considering only multiples of 3 and 5 is: {add_15_stuff(number)}")
