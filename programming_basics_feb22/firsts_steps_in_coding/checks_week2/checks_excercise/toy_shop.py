excursion = float(input())
number_puzzles = int(input())
number_puppets = int(input())
number_teddies = int(input())
number_minions = int(input())
number_trucks = int(input())

total = number_puzzles * 2.6 + number_puppets * 3 + number_teddies * 4.1 + number_minions * 8.2 \
        + number_trucks * 2

number = number_trucks + number_teddies + number_minions + number_puppets + number_puzzles

if number >= 50:
    total = total * 0.75
else:
    total = total

end_result = total * 0.9
money_left = 0
money_deficit = 0
if end_result - excursion >= 0:
    money_left = end_result - excursion
    print(f'Yes! {money_left:.2f} lv left.')
elif end_result - excursion < 0:
    money_deficit = excursion - end_result
    print(f'Not enough money! {money_deficit:.2f} lv needed.')