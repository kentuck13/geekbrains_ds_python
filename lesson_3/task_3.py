def bubble_sort(array: list):
    result = array
    for i in range(1, len(array)):
        for g in range(len(array)):
            current = result[i]
            next_item = result[g]

            if current > next_item:
                result[i], result[g] = next_item, current

    return result


def my_func_option_1(a, b, c, /):
    result = bubble_sort([a, b, c])
    return result[0] + result[1]


print(my_func_option_1(99, 2, 3))
