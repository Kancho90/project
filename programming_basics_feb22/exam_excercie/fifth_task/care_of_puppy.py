food = int(input())
food_eaten = 0

command = input()

while command != 'Adopted':
    food_eaten += int(command)
    command = input()

diff = food * 1000 - food_eaten
if diff >= 0:
    print(f'Food is enough! Leftovers: {abs(diff)} grams.')
else:
    print(f'Food is not enough. You need {abs(diff)} grams more.')