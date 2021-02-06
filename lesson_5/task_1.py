file = open('task_1.txt', 'w')
while True:
    data = input('Input data: ')

    if data == '':
        file.close()
        break
    print(data, '////')
    file.write(data + '\n')
