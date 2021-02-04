from functools import reduce

arr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def f(x, y):
    print(x, y)
    return x


list(map(f, arr))