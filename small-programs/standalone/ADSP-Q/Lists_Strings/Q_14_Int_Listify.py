import random

DEMO_INT = random.randint(500, 100000)


def int_to_list(a: int) -> list:
    return [x for x in str(a)]


if __name__ == '__main__':
    print(int_to_list(DEMO_INT))
