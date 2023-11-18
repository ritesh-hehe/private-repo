# Write a function that concatenates two lists.
# [a,b,c], [1,2,3] → [a,b,c,1,2,3]

'''import numpy


first_array = numpy.array(['a', 'b', 'c'])
second_array = numpy.array([1, 2, 3])


def concate_list(a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
    length_a = a.size
    length_b = b.size
    new_arr = numpy.empty(length_a+length_b)
    index_counter = 0
    for _ in range(length_a-1):
        new_arr[index_counter] = a[index_counter]
        index_counter += 1
    for _ in range(length_b-1):
        new_arr[index_counter] = b[index_counter]
        index_counter += 1
    return new_arr


print(concate_list(first_array, second_array))
'''

# Oh I forgot how arrays are limited to a single datatype... hehe
first_list = ['a', 'b', 'c']
second_list = [1, 2, 3]


def concate_lists(a: list, b: list) -> list:
    new_list = list()
    for elements in a:
        new_list.append(elements)
    for elements in b:
        new_list.append(elements)
    return new_list


if __name__ == '__main__':
    print(concate_lists(first_list, second_list))
