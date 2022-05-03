budget = float(input())
season = input()

price = 1
vehicle_type = ''
vehicle = ''

if budget <= 100:
    vehicle_type = 'Economy class'
    if season == 'Summer':
        vehicle = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        vehicle = 'Jeep'
        price = budget * 0.65
elif 100 < budget <= 500:
    vehicle_type = 'Compact class'
    if season == 'Summer':
        vehicle = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        vehicle = 'Jeep'
        price = budget * 0.8
else:
    vehicle_type = 'Luxury class'
    vehicle = 'Jeep'
    price = budget * 0.9

print(vehicle_type)
print(f'{vehicle} - {price:.2f}')
