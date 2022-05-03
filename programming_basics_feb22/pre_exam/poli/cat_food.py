number_of_cats = int(input())
group1 = 0
group2 = 0
group3 = 0
total_food = 0

for i in range (number_of_cats):
    food_eaten = float(input())
    total_food += food_eaten
    if 100 <= food_eaten < 200:
        group1 += 1
    elif 200 <= food_eaten < 300:
        group2 += 1
    else:
        group3 += 1

food_in_kg = total_food / 1000
price_food = food_in_kg * 12.45

print(f'Group 1: {group1} cats.')
print(f'Group 2: {group2} cats.')
print(f'Group 3: {group3} cats.')
print(f'Price for food per day: {price_food:.2f} lv.')