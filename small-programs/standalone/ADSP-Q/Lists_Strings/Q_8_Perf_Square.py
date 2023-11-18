# Write a function on_all that applies a function to every element of a list.
# Use it to print the first twenty perfect squares. The perfect squares can be found by multiplying
# each natural number with itself. The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16.
# Twelve for example is not a perfect square because there is no natural number m so that m\*m=12.
import numpy


first_20_number_array = numpy.array(range(1, 21))


def generate_perfect_square(a: numpy.ndarray) -> numpy.ndarray:
    perfect_square_array = numpy.empty(20, dtype=numpy.int16)
    for i in a:
        perfect_square_array[i-1] = i*i
    return perfect_square_array


if __name__ == '__main__':
    print(generate_perfect_square(first_20_number_array))
