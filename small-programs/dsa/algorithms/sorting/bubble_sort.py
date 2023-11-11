DEMO_LIST = [1, 1, 2, 5, 3, 7, 4, 11, 23, 109, 37, 54, 12, 109, 12]


def bubble_sort(sort_list: list, reverse=False) -> list:
    if reverse != True:
        for i in range(len(sort_list)-1):
            for j in range(len(sort_list)-1):
                if sort_list[j] > sort_list[j+1]:
                    sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
        return sort_list
    else:
        for i in range(len(sort_list)-1):
            for j in range(len(sort_list)-1):
                if sort_list[j] < sort_list[j+1]:
                    sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
        return sort_list


print(f"Before Sort -> {DEMO_LIST}")
print(f"After Sort -> {bubble_sort(DEMO_LIST)}")
print(f"Descending -> {bubble_sort(DEMO_LIST, reverse=True)}")
