# Write a function that rotates a list by k elements.
# For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].

# NOTE: That means if k=1, [2,3,4,5,6,1] and k=4, [5,6,1,2,3,4]

given_list = [1, 2, 3, 4, 5, 6]


def rotate_list(a: list, k: int) -> list:
    for index, _ in enumerate(a):
        if index < k:
            a.append(a.pop(0))
    return a


if __name__ == '__main__':
    print(rotate_list(given_list, 2))
