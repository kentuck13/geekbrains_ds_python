with open('task_2.txt') as file:
    line_count = 0
    for line in file:
        line = line.replace('\n', '')
        line_count += 1
        if line:
            print('Words count: %d' % len(line.split(' ')))
        else:
            print('Words count: 0')

    print('Total lines count: %d' % line_count)
