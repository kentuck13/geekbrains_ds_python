def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    result = x
    for i in range(abs(y) - 1):
        result *= x

    return 1 / result
