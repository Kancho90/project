price_shirt = float(input())
amount_needed = float(input())

price_shorts = price_shirt * 0.75
price_socks = price_shorts * 0.2
price_shoes = (price_shirt + price_shorts) * 2
total = price_shirt + price_shorts + price_socks + price_shoes
total *= 0.85

if total >= amount_needed:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total:.2f} lv.')
else:
    diff = abs(total - amount_needed)
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {diff:.2f} lv. more.')