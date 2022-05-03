import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

total_grape = y * x
grape_for_wine = total_grape * 0.4
wine_produced = grape_for_wine / 2.5

if wine_produced < z:
    wine_needed = math.floor(z - wine_produced)
    print(f'It will be a tough winter! More {wine_needed} liters wine needed.')
else:
    wine_produced = math.floor(wine_produced)
    wine_left = math.ceil(wine_produced - z)
    wine_per_person = math.ceil(wine_left / workers)
    print(f'Good harvest this year! Total wine: {wine_produced} liters.')
    print(f'{wine_left} liters left -> {wine_per_person} liters per person.')
