profit_required = float(input())

current_profit = 0
price = 0
while current_profit < profit_required:
    cocktail = input()
    if cocktail == 'Party!':
        break
    quantity = int(input())

    price = len(cocktail)
    if price * quantity % 2 != 0:
        current_profit += price * 0.75 * quantity
    else:
        current_profit += price * quantity

if current_profit < profit_required:
    print(f'We need {profit_required - current_profit:.2f} leva more.')
else:
    print(f'Target acquired.')

print(f'Club income - {current_profit:.2f} leva.')