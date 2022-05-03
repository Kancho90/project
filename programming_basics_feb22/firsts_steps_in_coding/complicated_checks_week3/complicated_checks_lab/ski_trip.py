stay = int(input())
type = input()
review = input()

nights = stay - 1

price_room = 18
price_app = 25
price_president = 35

if stay < 10:
    price_app = price_app * 0.7
    price_president = price_president * 0.9
elif 10 <= stay <= 15:
    price_app = price_app * 0.65
    price_president = price_president * 0.85
else:
    price_app = price_app * 0.5
    price_president = price_president * 0.8

total = 1
if type == 'room for one person':
    total = price_room * nights
elif type == 'apartment':
    total = price_app * nights
else:
    total = price_president * nights

if review == 'positive':
    total = total * 1.25
else:
    total = total * 0.9

print(f'{total:.2f}')