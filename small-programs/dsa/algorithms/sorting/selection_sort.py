DEMO_LIST = [1, 1, 2, 5, 3, 7, 4, 11, 23, 109, 37, 54, 12, 109, 12]


def selectionSort(sort_list: list) -> list:
    for i in range(len(DEMO_LIST)):
        for j in range(len(DEMO_LIST)):
            if sort_list[i] < sort_list[j]:
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    return sort_list


print(f"Before Sort -> {DEMO_LIST}")
print(f"After Sort -> {selectionSort(DEMO_LIST)}")
