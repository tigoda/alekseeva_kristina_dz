price = [56.7, 345.67, 34.6, 98.89, 123.87, 49.12, 50.1, 783.9, 22.4, 94.9, 5.2, 1001.45, 70.8, 25.1, 984.12]
print(id(price))
readable_prices = []
readable_prices_reversed = []
for el in price:
    r, kk = str(el).split('.')
    readable_prices.append(f'{r} руб {int(kk):02d} коп')
print(', '.join(readable_prices))
price.sort()
print(price)
print(id(price))
readable_prices_reversed.extend(sorted(price, reverse=True))
print(readable_prices_reversed)
print(readable_prices_reversed[:5])
