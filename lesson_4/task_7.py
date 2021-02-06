from functools import reduce


def fact(n):
    numbers = range(1, n + 1)
    result = 1

    for current in numbers:
        result *= current

        yield result


for el in fact(4):
    print(el)
