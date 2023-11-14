# Write a function that returns the largest element in a list.

import random
import numpy


random_array = numpy.array(random.sample(range(1, 10001), 50))


def return_largest_element(arr: numpy.ndarray) -> int:
    return arr.max()


print(
    f"The largest element this time is: {return_largest_element(random_array)}")
