stage = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_picture = input()

price = 1

if stage == 'Quarter final':
    if ticket_type == 'Standard':
        price = 55.5
    elif ticket_type == 'Premium':
        price = 105.2
    elif ticket_type == 'VIP':
        price = 118.9
elif stage == 'Semi final':
    if ticket_type == 'Standard':
        price = 75.88
    elif ticket_type == 'Premium':
        price = 125.22
    elif ticket_type == 'VIP':
        price = 300.4
elif stage == 'Final':
    if ticket_type == 'Standard':
        price = 110.1
    elif ticket_type == 'Premium':
        price = 160.66
    elif ticket_type == 'VIP':
        price = 400

total = price * number_of_tickets


if total > 4000:
    total =  total * 0.75
elif 2500 < total <= 4000:
    total  = total * 0.9
    if trophy_picture == 'Y':
        total += number_of_tickets * 40
elif total < 2500 and trophy_picture == 'Y':
    total += number_of_tickets * 40

print(f'{total:.2f}')