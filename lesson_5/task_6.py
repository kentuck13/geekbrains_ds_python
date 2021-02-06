import re

obj = {}
with open('task_6.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        subject, study_process = line.split(': ')

        count = sum(
            [
                int(g) for i in study_process.split(' ')
                if (g := re.sub('\D', '', i))
            ]
        )

        obj[subject] = count

print(obj)
