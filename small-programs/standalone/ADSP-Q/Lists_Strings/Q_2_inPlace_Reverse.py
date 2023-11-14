# Write function that reverses a list, preferably in place.

import random
import numpy


random_array = numpy.array(random.sample(range(1, 10001), 50))


def reverse_array(arr: numpy.ndarray) -> numpy.ndarray:
    # Guess this is as much in-place as it goes....
    # where does it store the data though? buffer?
    # man, how they even think of stuff like this?
    # can't comprehend with my double digit IQ hehe
    return arr[::-1]


print(f"Array Before Reverse:\n{random_array}")
print(f"Array After Reverse:\n{reverse_array(random_array)}")
