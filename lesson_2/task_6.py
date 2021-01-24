products = []

while True:
    name = input('Product name: ')
    price = input('Product price: ')
    amount = input('Product amount: ')
    measurement = input('Product measurement: ')
    print('-----------------')

    products.append((
        len(products),
        {
            'name': name,
            'price': price,
            'amount': amount,
            'measurement': measurement
        }
    ))

    if len(products) == 3:
        analytics = {
            'name': set(),
            'price': set(),
            'amount': set(),
            'measurement': set()
        }
        for index, product in products:
            analytics['name'].add(product['name'])
            analytics['price'].add(product['price'])
            analytics['amount'].add(product['amount'])
            analytics['measurement'].add(product['measurement'])

        analytics['name'] = list(analytics['name'])
        analytics['price'] = list(analytics['price'])
        analytics['amount'] = list(analytics['amount'])
        analytics['measurement'] = list(analytics['measurement'])

        print(analytics)
        break
