budget = float(input())
litres_needed = float(input())
day = input()

total = litres_needed * 2.1 + 100
if day == "Saturday":
    total_discounted = total * 0.9
elif day == "Sunday":
    total_discounted = total * 0.8

if budget >= total_discounted:
    money_left = budget - total_discounted
    print(f'Safari time! Money left: {money_left:.2f} lv.')
else:
    money_needed = total_discounted - budget
    print(f'Not enough money! Money needed: {money_needed:.2f} lv.')