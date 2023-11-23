# Write functions that add, subtract, and multiply two numbers in their digit-list representation (and return a new digit list).
# If you’re ambitious you can implement Karatsuba multiplication. Try different bases.

# NOTE: Karatsuba is a recursive algorithm....ahhh ;-;
# NOTE_2: I don't understand the point of Karatsuba in this scenario

first_num = 146
second_num = 235


def add_margin() -> None:
    for _ in range(100):
        print("-", end="")
    print()


def int_to_list(a: int) -> list:
    return [int(x) for x in str(a)]


def list_to_int(a: list) -> int:
    return "".join([str(x) for x in a])


def add_list(a: list, b: list) -> list:
    new_list = list()
    if len(a) == len(b):
        for i in range(len(a)):
            new_list.append(a[i]+b[i])
    else:
        index_counter = 0
        if len(a) > len(b):
            for i in range(len(b)):
                new_list.append(a[i]+b[i])
                index_counter += 1
            new_list.append(a[index_counter::1])
        else:
            for i in range(len(a)):
                new_list.append(a[i]+b[i])
                index_counter += 1
            new_list.append(b[index_counter::1])
    return new_list


def subtract_list(a: list, b: list) -> list:
    new_list = list()
    if len(a) == len(b):
        for i in range(len(a)):
            new_list.append(a[i]-b[i])
    else:
        index_counter = 0
        if len(a) > len(b):
            for i in range(len(b)):
                new_list.append(a[i]-b[i])
                index_counter += 1
            new_list.append(a[index_counter::1])
        else:
            for i in range(len(a)):
                new_list.append(a[i]-b[i])
                index_counter += 1
            new_list.append(b[index_counter::1])
    return new_list


def normal_multiply_list(a: list, b: list) -> list:
    new_list = list()
    if len(a) == len(b):
        for i in range(len(a)):
            new_list.append(a[i]*b[i])
    else:
        index_counter = 0
        if len(a) > len(b):
            for i in range(len(b)):
                new_list.append(a[i]*b[i])
                index_counter += 1
            new_list.append(a[index_counter::1])
        else:
            for i in range(len(a)):
                new_list.append(a[i]*b[i])
                index_counter += 1
            new_list.append(b[index_counter::1])
    return new_list


def divide_list(a: list, b: list) -> list:
    new_list = list()
    if len(a) == len(b):
        for i in range(len(a)):
            if b[i] != 0:
                new_list.append(a[i]//b[i])
            else:
                new_list.append(f"{a[i]}/0")
    else:
        index_counter = 0
        if len(a) > len(b):
            for i in range(len(b)):
                if b[i] != 0:
                    new_list.append(a[i]//b[i])
                else:
                    new_list.append(f"{a[i]}/0")
                index_counter += 1
            new_list.append(a[index_counter::1])
        else:
            for i in range(len(a)):
                if a[i] != 0:
                    new_list.append(b[i]//a[i])
                else:
                    new_list.append(f"{b[i]}/0")
                index_counter += 1
            new_list.append(b[index_counter::1])
    return new_list


if __name__ == '__main__':
    add_margin()
    print(f"First Number: {first_num}")
    print(f"Second Number: {second_num}")
    add_margin()
    print(
        f"After adding: {add_list(int_to_list(first_num), int_to_list(second_num))}, and in integer form {list_to_int(add_list(int_to_list(first_num), int_to_list(second_num)))}")
    print(
        f"After subtraction: {subtract_list(int_to_list(first_num), int_to_list(second_num))}, and in integer form {list_to_int(subtract_list(int_to_list(first_num), int_to_list(second_num)))}")
    print(
        f"After multiplication: {normal_multiply_list(int_to_list(first_num), int_to_list(second_num))}, and in integer form {list_to_int(normal_multiply_list(int_to_list(first_num), int_to_list(second_num)))}")
    print(f"After division: {divide_list(int_to_list(first_num), int_to_list(second_num))}, and in integer form {list_to_int(divide_list(int_to_list(first_num), int_to_list(second_num)))}")
