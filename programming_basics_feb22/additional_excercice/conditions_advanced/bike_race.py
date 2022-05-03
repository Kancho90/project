junior_contestants = int(input())
senior_contestants = int(input())
race_type = input()

total = 1

if race_type == 'trail':
    total = junior_contestants * 5.5 + senior_contestants * 7
elif race_type == 'cross-country':
    total = junior_contestants * 8 + senior_contestants * 9.5
    if junior_contestants + senior_contestants >= 50:
        total = total * 0.75
elif race_type == 'downhill':
    total = junior_contestants * 12.25 + senior_contestants * 13.75
elif race_type == 'road':
    total = junior_contestants * 20 + senior_contestants * 21.5

money = total * 0.95
print(f'{money:.2f}')