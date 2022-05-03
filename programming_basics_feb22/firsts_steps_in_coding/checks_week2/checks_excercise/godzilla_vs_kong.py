film_budged = float(input())
extras = int(input())
price_clothes = float(input())

decor_price  = film_budged * 0.1
total_clothes = extras  * price_clothes

if extras > 150:
    total_clothes = total_clothes * 0.9
else:
    total_clothes = total_clothes * 1

total_spent = decor_price + total_clothes
money_left = film_budged - total_spent
money_needed =  total_spent - film_budged

if money_left >= 0:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
if  money_left < 0:
    print('Not enough money!')
    print(f"Wingard needs {money_needed:.2f} leva more.")