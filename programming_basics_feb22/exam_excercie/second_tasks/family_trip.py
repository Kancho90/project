budget = float(input())
nights = int(input())
price_for_a_night = float(input())
extra_spend = float(input())

price_for_sleep = price_for_a_night * nights
if nights > 7:
    price_for_sleep = price_for_sleep * 0.95

extra_total = extra_spend / 100 * budget
total_vacation = extra_total + price_for_sleep

if budget >= total_vacation:
    money_left = budget - total_vacation
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')
else:
    money_needed = total_vacation - budget
    print(f'{money_needed:.2f} leva needed.')