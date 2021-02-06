with open('task_4_en.txt') as file:
    with open('task_4_ru.txt', 'w') as translate_file:
        for line in file:
            line = line.lower()

            if 'one' in line:
                line = line.replace('one', 'Один')
            if 'two' in line:
                line = line.replace('two', 'Два')
            if 'three' in line:
                line = line.replace('three', 'Три')
            if 'four' in line:
                line = line.replace('four', 'Четыре')

            translate_file.write(line)
