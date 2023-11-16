# Write a function that returns the elements on odd positions in a list.
import numpy
import random


random_array = numpy.array(random.sample(range(1, 100), 50))


def print_odd_indexes(arr: numpy.ndarray) -> None:
    print("Elements in Odd Indexes: ")
    for odd_index in range(0, len(arr), +2):
        print(arr[odd_index], end=", ")


if __name__ == "__main__":
    print_odd_indexes(random_array)
