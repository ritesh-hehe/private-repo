# Write a function that computes the running total of a list.

import numpy
import random


random_array = numpy.array(random.sample(range(1, 100), 50))


def compute_sum(arr: numpy.ndarray) -> None:
    print(f"The array generated:\n{arr}")
    print(f"The running sum of the array is:\n{arr.cumsum()}")


if __name__ == "__main__":
    compute_sum(random_array)
