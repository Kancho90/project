money_needed = float(input())
money = float(input())

days_spending = 0
days_saving = 0

while money < money_needed and days_spending < 5:
    action = input()
    money_action = float(input())
    days_saving += 1

    if action == 'save':
        money += money_action
        days_spending = 0
    elif action == 'spend':
        days_spending += 1
        if money < money_action:
            money = 0
        else:
            money -= money_action

if days_spending == 5:
    print("You can't save the money.")
    print(days_saving)

if money >= money_needed:
    print(f'You saved the money for {days_saving} days.')