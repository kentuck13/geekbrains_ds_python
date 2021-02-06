from functools import reduce

even = range(100, 1001, 2)

print(reduce(lambda x, y: x * y, even))
