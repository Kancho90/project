locations = int(input())

for i in range(locations):
    average_gold_expected = float(input())
    gold_collected = 0
    days = int(input())
    for j in range (days):
        daily_gold = float(input())
        gold_collected += daily_gold
    actual_average = gold_collected / days
    if actual_average >= average_gold_expected:
        print(f'Good job! Average gold per day: {actual_average:.2f}.')
    else:
        print(f'You need {average_gold_expected - actual_average:.2f} gold.')