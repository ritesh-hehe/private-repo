import random
import time

# MAIN LIST
DEMO_LIST = random.sample(range(1, 101), 10)


# BEGIN FUNCTION ZOME
def addSpaces(spaceRange=20) -> None:
    for _ in range(spaceRange):
        print(end=" ")


def addDottedLines() -> None:
    for _ in range(80):
        print("-", end="")
    print()


def showIndex(a_list: list) -> list:
    indexList = list()
    for index, _ in enumerate(a_list):
        indexList.append(index)
    return indexList


def showMenu() -> None:
    print("Press 1 to sort the list(sort or sorted)")
    print("Press 2 to delete a specific element(remove)")
    print("Press 3 to pop element(pop)")
    print("Press 4 to add elements to list(append or extend)")
    print("Press 5 to reverse list([::-1])")
    print("Press 6 to clear list(clear)")
    print("Press 7 to exit program(break)\n")
# END FUNCTION ZONE


# CLI START
print("Welcome To Menu!")
while True:
    time.sleep(0.5)
    addDottedLines()
    showMenu()
    addSpaces()
    try:
        print(DEMO_LIST)
    except NameError:
        print("List has ceased to exist....")
    addDottedLines()
    query = int(input("INPUT: "))
    match(query):

        case 1:
            sortType = input("Ascending(a) or Descending(d): ")
            if sortType not in "aAdD":
                print("Invalid input..")
            else:
                if sortType in "aA":
                    DEMO_LIST.sort()
                else:
                    DEMO_LIST.sort(reverse=True)

        case 2:
            delValue = int(input("Enter value to delete: "))
            try:
                DEMO_LIST.remove(delValue)
            except ValueError:
                print("Given value doesn't exist")

        case 3:
            addDottedLines()
            addSpaces()
            print(DEMO_LIST)
            addSpaces(20 - len('Index -> '))
            print(f'Index -> {showIndex(DEMO_LIST)}')
            delIndex = int(input("Enter index to pop.."))
            try:
                print(f"Popped Value: {DEMO_LIST.pop(delIndex)}")
            except IndexError:
                print("Invalid Index")

        case 4:
            print("Enter values to put into list: ")
            userValues = [int(x) for x in input("Enter the numbers: ").split()]
            DEMO_LIST.extend(userValues)
            print("List extended!")

        case 5:
            DEMO_LIST = DEMO_LIST[::-1]

        case 6:
            DEMO_LIST.clear()

        case 7:
            input("Press any key to exit...")
            break

        case default:
            print("Invalid Input...")
