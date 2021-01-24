seasons = {
    (12, 1, 2): 'Зима',
    (3, 4, 5): 'Весна',
    (6, 7, 8): 'Лето',
    (9, 10, 11): 'Осень',
}

user_number = int(input('Input number: '))

for key, value in seasons.items():
    if user_number in key:
        print(value)
        break
