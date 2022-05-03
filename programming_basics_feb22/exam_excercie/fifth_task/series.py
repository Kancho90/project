budget = float(input())
number_of_tvseries = int(input())

total = 0

for i in range(number_of_tvseries):
    name = input()
    price = float(input())
    if name == 'Thrones':
        total += price * 0.5
    elif name == 'Lucifer':
        total += price * 0.6
    elif name == 'Protector':
        total += price * 0.7
    elif name == 'TotalDrama':
        total += price * 0.8
    elif name == 'Area':
        total += price * 0.9
    else:
        total += price

diff = abs(budget - total)
if budget >= total:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')
