import random
import time


DEMO_LIST = [1, 1, 2, 5, 3, 7, 4, 11, 23, 109, 37, 54, 12, 109, 12]


def generateBadList() -> list:
    '''Generate a 10k element list with elements from [1-1000]'''
    RANDOM_LIST = list()
    for _ in range(10000):
        RANDOM_LIST.append(random.randint(1, 1000))
    return RANDOM_LIST


def linearSearch(a: int, b: list) -> str:
    listIndexes = list()
    for index, element in enumerate(b):
        if element == a:
            listIndexes.append(index)
    if len(listIndexes) == 0:
        return "Search did not bring up any results.... :("
    else:
        return f"Element {a} found in index(es) {listIndexes}"


search_query = int(input("Enter number to search: "))
print(f"Press 1 if you want to search in DEMO_LIST (length: {len(DEMO_LIST)})")
print("Press 2 if you want to search in random generated list (length: 10k)")
query = int(input("INPUT: "))
TIME_PROG_EXEC = time.perf_counter()
match(query):
    case 1:
        print(linearSearch(search_query, DEMO_LIST))
        print(
            f"Time Taken:{round(time.perf_counter()-TIME_PROG_EXEC, 10)} second(s)")
    case 2:
        randGenList = generateBadList()
        print(linearSearch(search_query, randGenList))
        print(
            f"Time Taken:{round(time.perf_counter()-TIME_PROG_EXEC, 10)} second(s)")
    case default:
        print("Invalid Input")
