import random
import time

DEMO_LIST = [1, 1, 2, 5, 3, 7, 4, 11, 23, 109, 37, 54, 12, 109, 12]
RANDOM_LIST = random.sample(range(50000), 10000)


def binary_search(search_query: int, listToSearch=DEMO_LIST) -> str:
    MINIMUM_INDEX = 0
    MAXIMUM_INDEX = len(listToSearch)-1

    while MINIMUM_INDEX <= MAXIMUM_INDEX:
        MEDIAN = MINIMUM_INDEX + ((MAXIMUM_INDEX-MINIMUM_INDEX)//2)
        if listToSearch[MEDIAN] == search_query:
            return f"Number {listToSearch[MEDIAN]} exists"
        else:
            if listToSearch[MEDIAN] < search_query:
                MINIMUM_INDEX = MEDIAN + 1
            else:
                MAXIMUM_INDEX = MEDIAN - 1
    return f"Number {search_query} doesn't exist"


search_query = int(input("Enter number to search: "))
print(f"Press 1 if you want to search in DEMO_LIST (length: {len(DEMO_LIST)})")
print("Press 2 if you want to search in random generated list (length: 10k)")
query = int(input("INPUT: "))
TIME_PROG_EXEC = time.perf_counter()
match(query):
    case 1:
        print(binary_search(search_query, listToSearch=sorted(DEMO_LIST)))
        print(
            f"Time Taken:{round(time.perf_counter()-TIME_PROG_EXEC, 10)} second(s)")
    case 2:
        print(binary_search(search_query, listToSearch=sorted(RANDOM_LIST)))
        print(
            f"Time Taken:{round(time.perf_counter()-TIME_PROG_EXEC, 10)} second(s)")
    case default:
        print("Invalid Input")
