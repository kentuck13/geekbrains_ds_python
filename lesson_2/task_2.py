data = []

while True:
    item = input('Input item: ')
    if item:
        data.append(item)

        if not len(data) % 2:
            data[-1], data[-2] = data[-2], data[-1]
        print(data)
