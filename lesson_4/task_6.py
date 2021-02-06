import itertools

for i in itertools.count(10):
    print(i)
    if i == 20:
        break

count = 0
for i in itertools.cycle('HelloWorld'):
    count += 1
    if count == 20:
        break
    print(i)
