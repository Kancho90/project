budget = float(input())
category = input()
people = int(input())

price_vip = 499.99
price_normal = 249.99

total_price = 1
travel = 1

if people <= 4:
    travel = budget * 0.75
elif 4 < people <= 9:
    travel = budget * 0.6
elif 10 <= people <= 24:
    travel = budget * 0.5
elif 25 <= people < 50:
    travel = budget * 0.4
elif people >= 50:
    travel = budget * 0.25

if category == 'VIP':
    total_price = price_vip * people
elif category == 'Normal':
    total_price = price_normal * people

total_trip = total_price + travel
money = abs(budget - total_trip)
if budget >= total_trip:
    print(f'Yes! You have {money:.2f} leva left.')
else:
    print(f'Not enough money! You need {money:.2f} leva.')
