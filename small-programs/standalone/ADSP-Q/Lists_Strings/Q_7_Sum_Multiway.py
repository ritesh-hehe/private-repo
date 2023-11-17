# Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
import numpy
import random


random_array = numpy.array(random.sample(range(1, 100), 50))
sum_array_recursion = 0


def for_loop_method(arr: numpy.ndarray) -> int:
    sum_array = 0
    for i in arr:
        sum_array += i
    return sum_array


def while_loop_method(arr: numpy.ndarray) -> int:
    sum_array = 0
    length_array = len(arr)
    while length_array:
        sum_array += arr[-length_array]
        length_array -= 1
    return sum_array


def recursion_method(arr: numpy.ndarray, length_array: int) -> int:
    # Now this is tricky, as I have never bothered to tackle recursion problems
    # Call it a personal issue of mine, but I never liked recursion...

    # ..after 30 whole minutes...I swear I feel so demotivated :(
    if length_array == len(arr)-1:
        return arr[length_array]
    else:
        return arr[length_array] + recursion_method(arr, length_array+1)


if __name__ == '__main__':
    print(f"Actual array: \n{random_array}")
    print(f"Using For Loop: {for_loop_method(random_array)}")
    print(f"Using While Loop: {while_loop_method(random_array)}")
    # Jeez, that took me a while....hehe, feels good!
    print(f"Using Recursion Method: {recursion_method(random_array, 0)}")
