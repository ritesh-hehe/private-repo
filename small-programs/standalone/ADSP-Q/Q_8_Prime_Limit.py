# Write a program that prints all prime numbers. (Note: if your programming language does not support
# arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

# NOTE: I tried using multiprocessing, but ITERATION_COUNTER tends to be 0, when it is run. I don't know how to fix it

import math
import time


ITERATION_COUNTER = 0


def verify_prime(n: int) -> None:
    global ITERATION_COUNTER
    flag = True
    # n/2 considering digits just tend to repeat(no idea what it is called in math)
    # and ceil() considering floor will round it to the lowest, round() has a chance of doing the same
    # but that will skip n-1th digit, effecitvely breaking the code...i think
    for i in range(2, math.ceil(n/2)):
        ITERATION_COUNTER += 1
        if n % i == 0:
            flag = False
            break
    if flag:
        print(n)


if __name__ == '__main__':
    PROG_START = time.perf_counter()
    # that's a dang big number if I say so myself...considering it takes over 20sec to run on my workspace
    MAX_HEADER = int(10e4)  # int(10e5)
    for i in range(2, MAX_HEADER):
        verify_prime(i)
    print(f"Time taken: {round(time.perf_counter() - PROG_START,10)}")
    print(f"Iterations occured: {ITERATION_COUNTER}")
