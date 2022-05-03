best_player = ''
number_of_goals = 0

for i in range(1,100000):
    name = input()
    if name == 'END':
        break
    goals = int(input())
    if goals > number_of_goals:
        number_of_goals = goals
        best_player = name
    if goals >= 10:
        break

print(f'{best_player} is the best player!')
if number_of_goals < 3:
    print(f'He has scored {number_of_goals} goals.')
else:
    print(f'He has scored {number_of_goals} goals and made a hat-trick !!!')