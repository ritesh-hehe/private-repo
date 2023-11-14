# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
# Haha, had a field day with this one!

PROCESS_LIST = list()
PREVIOUS_SUM = 0  # Counter value to keep record of the summations


def display_process(n: int) -> None:
    global PREVIOUS_SUM
    PROCESS_LIST.append(f"{PREVIOUS_SUM} + {n} = {n+PREVIOUS_SUM}")


def sum_till_n(n: int) -> int:
    global PREVIOUS_SUM
    for elements_till_n in range(1, n):
        display_process(elements_till_n)
        PREVIOUS_SUM += elements_till_n
    return PREVIOUS_SUM


n = int(input("Enter the value of n: "))
print(f"The sum of numbers till {n} is: {sum_till_n(n+1)}")
print("Would you like to see the process? y/n: ")
if input() in 'yY':
    print("Process is: ")
    print("[Sum + M = Value]")
    for processes in PROCESS_LIST:
        print(processes)
else:
    print("Thanks for running me :D")
