import math

magnolias = int(input())
zumbuli = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())

magnolias_price = magnolias * 3.25
zumbuli_price = zumbuli * 4
roses_price = roses * 3.5
cactuses_price = cactuses * 8
total = magnolias_price + zumbuli_price + roses_price + cactuses_price
profit = total * 0.95

if profit >= gift_price:
    money_left = math.floor(profit - gift_price)
    print(f'She is left with {money_left} leva.')
else:
    money_needed = math.ceil(gift_price - profit)
    print(f'She will have to borrow {money_needed} leva.')

