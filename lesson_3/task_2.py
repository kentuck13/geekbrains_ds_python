def func(*, name, last_name, year_of_birth, city, email, phone):
    print(f'{name}, {last_name}, {year_of_birth}, {city}, {email}, {phone}')


func(name='Hello', last_name='world', year_of_birth='19', city='Moscow',
     email='mymail', phone='myphone')
