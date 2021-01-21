number = input('Input number: ')

# First method
current_index = 0
max_index = len(number)
the_biggest_numeral = 0

while current_index < max_index:
    current_numeral = int(number[current_index])
    if the_biggest_numeral < current_numeral:
        the_biggest_numeral = current_numeral

    current_index += 1

print(the_biggest_numeral)

# Second method
print(max(int(i) for i in number))
