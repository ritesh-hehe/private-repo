# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed. It counts only as one try if they
# input the same number multiple times consecutively.
import random


CPU_GEN_RANDOM_NUM = random.randint(1, 100)
REPEAT_NUMBER_LIST = list()
TRIES_TAKEN = 1
GAME_OVER = False


def guess_function(n: int) -> None:
    # There is never enough global vars hehe
    global CPU_GEN_RANDOM_NUM
    global REPEAT_NUMBER_LIST
    global TRIES_TAKEN
    global GAME_OVER
    if n != CPU_GEN_RANDOM_NUM:
        if n in REPEAT_NUMBER_LIST:
            print(f"You have already guessed {n}. Guess something else...")
        else:
            if n > CPU_GEN_RANDOM_NUM:
                REPEAT_NUMBER_LIST.append(n)
                TRIES_TAKEN += 1
                print("Guess Lower")
            else:
                REPEAT_NUMBER_LIST.append(n)
                TRIES_TAKEN += 1
                print("Guess Higher")
    else:
        print(
            f"Nice! You got the number {CPU_GEN_RANDOM_NUM} in {TRIES_TAKEN} try(ies?)")


print("Welcome to Guess Game hehe!")
while True:
    print(f"Debug(totally not dev cheat :D): {CPU_GEN_RANDOM_NUM}")
    USER_GIVEN_VALUE = int(input("Enter number from 1-100: "))
    guess_function(USER_GIVEN_VALUE)
    if GAME_OVER:
        input("Press any key to exit....")
        break
