destination = input()

while destination != 'End':
    money_needed = float(input())
    money_gathered = 0
    while money_gathered < money_needed:
        money = float(input())
        money_gathered += money
    print(f'Going to {destination}!')
    destination = input()
    money_gathered = 0