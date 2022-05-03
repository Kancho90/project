months = int(input())

electricity = 0
internet = months * 15
water = months * 20
other = 0

for i in range(months):
    monthly_elect = float(input())
    electricity += monthly_elect
    other += (15 + 20 + monthly_elect) * 1.2

average = (electricity + water + internet + other) / months

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')

