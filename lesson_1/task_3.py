number = int(input('Input number: '))

# First method
print(
    number +
    int('%d%d' % (number, number)) +
    int('%d%d%d' % (number, number, number))
)

# Second method
print(sum([int(('%d' % number) * i) for i in range(1, 4)]))
