# Write a function that combines two lists by alternatingly taking elements
# e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

first_list = ['a', 'b', 'c']
second_list = [1, 2, 3]


def alt_concate_lists(a: list, b: list) -> list:
    ''' Alternatingly concates elements of two lists.
    If one list is bigger in length than the other, continue alternate concate
    till smaller list length is reached, where rest elements of larger elements will be
    concatenated normally...'''
    new_list = list()
    if len(a) == len(b):
        for i in range(len(a)):
            new_list.append(a[i])
            new_list.append(b[i])
    else:
        index_counter = 0
        if len(a) > len(b):
            for i in range(len(b)):
                new_list.append(a[i])
                new_list.append(b[i])
                index_counter += 1
            new_list.extend([x for x in a[index_counter: len(a): 1]])
        else:
            for i in range(len(a)):
                new_list.append(a[i])
                new_list.append(b[i])
                index_counter += 1
            new_list.extend([x for x in b[index_counter: len(b): 1]])
    return new_list


if __name__ == '__main__':
    print(alt_concate_lists(first_list, second_list))
