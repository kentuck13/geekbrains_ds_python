data = []
while True:
    input_data = input('Input: ').split(' ')
    data.extend([i for i in input_data if i.isdigit()])

    if not all(i.isdigit() for i in input_data):
        print(sum([int(i) for i in data]))
        break
    print(sum([int(i) for i in data]))
