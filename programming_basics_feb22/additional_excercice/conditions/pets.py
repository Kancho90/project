import math

days = int(input())
food_left = int(input())
food_for_doggy = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())

total_dog = food_for_doggy * days
total_cat = food_for_cat * days
total_turtle = food_for_turtle * days / 1000
total_for_all = total_turtle + total_cat + total_dog

if food_left >= total_for_all:
    remaining_food = math.floor(food_left - total_for_all)
    print(f'{remaining_food} kilos of food left.')
else:
    food_needed = math.ceil(total_for_all - food_left)
    print(f'{food_needed} more kilos of food are needed.')