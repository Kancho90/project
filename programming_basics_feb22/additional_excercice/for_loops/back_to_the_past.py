money = float(input())
year = int(input())
money_spent = 0
age = 18

for j in range(1800, year + 1):
    if j != 1800:
        age += 1
    if j % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * age

diff = abs(money - money_spent)
if money >= money_spent:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')