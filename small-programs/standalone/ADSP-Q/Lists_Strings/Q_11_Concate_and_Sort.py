# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].

first_list = [1, 4, 6]
second_list = [2, 3, 5]


def concate_and_sort(a: list, b: list) -> list:
    new_list = list()
    new_list.extend(a)
    new_list.extend(b)
    return sorted(new_list)


if __name__ == '__main__':
    print(concate_and_sort(first_list, second_list))
