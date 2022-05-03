food_bought = int(input())

eaten_food = input()
total = 0
food_bought_in_gr = food_bought * 1000
while eaten_food != 'Adopted':
    total += int(eaten_food)

    eaten_food = input()

diff = abs(food_bought_in_gr - total)
if food_bought_in_gr >= total:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')