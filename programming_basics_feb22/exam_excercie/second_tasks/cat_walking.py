minutes_walk = int(input())
number_of_walks = int(input())
calories = int(input())

calories_burnt = minutes_walk * 5 * number_of_walks

if calories_burnt >= (calories / 2):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.')