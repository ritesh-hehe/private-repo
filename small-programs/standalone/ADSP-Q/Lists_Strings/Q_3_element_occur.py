# Write a function that checks whether an element occurs in a list.

# Basically, implement a searching algo...skibbidi boop!
import random
import numpy


random_array = numpy.array(random.sample(range(1, 100), 50))


def linearSearch(arr: numpy.ndarray, item: int) -> str:
    occurance_value = 0
    for i in arr:
        if i == item:
            occurance_value += 1
    if occurance_value != 0:
        return f"Item {item} occured {occurance_value} time(s) in the array"
    else:
        return f"Item {item} doesn't exist in array"


print(linearSearch(random_array, 50))
