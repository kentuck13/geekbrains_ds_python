import numpy

with open('task_3.txt') as file:
    salaries = []

    for line in file:
        line = line.replace(' ', '')
        name, salary = line.split('-')
        print(name, salary)
        salaries.append(int(salary))

print(f'Middle salary: {numpy.median(salaries)}')
