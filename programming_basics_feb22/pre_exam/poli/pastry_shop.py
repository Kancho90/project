sweet = input()
order_count = int(input())
day_before_christmas = int(input())

price = 0
if sweet == 'Cake':
    if day_before_christmas <= 15:
        price = 24
    else:
        price = 28.7
elif sweet == 'Souffle':
    if day_before_christmas <= 15:
        price = 6.66
    else:
        price = 9.8
elif sweet == 'Baklava':
    if day_before_christmas <= 15:
        price = 12.6
    else:
        price = 16.98

total = price * order_count
if day_before_christmas <= 22:
    if 100 <= total <= 200:
        total *= 0.85
    elif total > 200:
        total *= 0.75
    if day_before_christmas <= 15:
        total *= 0.9

print(f'{total:.2f}')