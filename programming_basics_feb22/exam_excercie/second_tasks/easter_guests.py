import math

guests = int(input())
budget = int(input())

kozunaci_needed = math.ceil(guests / 3)
eggs_needed = guests * 2
price_kozunaci = kozunaci_needed * 4
price_eggs = eggs_needed * 0.45
total = price_eggs + price_kozunaci

if budget >= total:
    money_left = budget - total
    print(f'Lyubo bought {kozunaci_needed} Easter bread and {eggs_needed} eggs.')
    print(f'He has {money_left:.2f} lv. left.')
else:
    money_needed = total - budget
    print("Lyubo doesn't have enough money.")
    print(f'He needs {money_needed:.2f} lv. more.')