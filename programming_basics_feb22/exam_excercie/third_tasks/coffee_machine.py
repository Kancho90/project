drink = input()
sugar_selection = input()
number_of_drinks = int(input())

price = 1

if drink == 'Espresso':
    if sugar_selection == 'Without':
        price = 0.9
    elif sugar_selection == 'Normal':
        price = 1
    else:
        price = 1.2
elif drink == 'Cappuccino':
    if sugar_selection == 'Without':
        price = 1
    elif sugar_selection == 'Normal':
        price = 1.2
    else:
        price = 1.6
else:
    if sugar_selection == 'Without':
        price = 0.5
    elif sugar_selection == 'Normal':
        price = 0.6
    else:
        price = 0.7

total = price * number_of_drinks
if sugar_selection == 'Without':
    total = total * 0.65

if drink == 'Espresso' and number_of_drinks >= 5:
    total  = total  * 0.75

if total > 15:
    total = total * 0.8

print(f'You bought {number_of_drinks} cups of {drink} for {total:.2f} lv.')