numbers = []
with open('task_5.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        if line:
            numbers.extend([int(i) for i in line.split(' ') if i])


print(sum(numbers))
