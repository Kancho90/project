quantity = int(input())
type = input()
delivery = input()

price = 1
discount = 1

if type == '90X130':
    price = 110
    if 30 < quantity <= 60:
        discount = 0.95
    elif quantity > 60:
        discount = 0.92
elif type == '100X150':
    price = 140
    if 40 < quantity <= 80:
        discount = 0.94
    elif quantity > 80:
        discount = 0.9
elif type == '130X180':
    price = 190
    if 20 < quantity <= 50:
        discount = 0.93
    elif quantity > 50:
        discount = 0.88
elif type == '200X300':
    price = 250
    if 25 < quantity <= 50:
        discount = 0.91
    elif quantity > 50:
        discount = 0.86

total = quantity * price * discount

if delivery == 'With delivery':
    total += 60

if quantity > 99:
    total = total * 0.96

if quantity < 10:
    print('Invalid order')
else:
    print(f'{total:.2f} BGN')