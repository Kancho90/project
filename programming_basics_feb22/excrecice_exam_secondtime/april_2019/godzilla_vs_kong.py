budget = float(input())
statists = int(input())
price_for_clothes = float(input())
decor = budget * 0.1

total_clothes = price_for_clothes * statists
if statists > 150:
    total_clothes *= 0.9

total = decor + total_clothes
diff = abs(budget - total)
if budget >= total:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')