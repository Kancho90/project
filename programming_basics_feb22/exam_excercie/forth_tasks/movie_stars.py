budget = float(input())

remaining_budget = budget
while True:
    name = input()

    if name == 'ACTION':
        break
    if len(name) > 15:
        remaining_budget *= 0.8
    else:
        salary = float(input())
        remaining_budget -= salary

    if remaining_budget < 0:
        break

if remaining_budget  >= 0:
    print(f'We are left with {remaining_budget:.2f} leva.')
else:
    print(f'We need {abs(remaining_budget):.2f} leva for our actors.')