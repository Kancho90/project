budget = float(input())
season = input()

location = ''
stay = ''
price = 1

if budget <= 1000:
    stay = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    stay = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.8
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.6
else:
    stay = 'Hotel'
    price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {stay} - {price:.2f}')