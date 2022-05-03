student = 0
kid = 0
standard = 0
name = input()
while name != 'Finish':
    capacity = int(input())
    current_tickets = 0
    ticket_type = ""

    while capacity > current_tickets and ticket_type != 'End':
        ticket_type = input()

        if ticket_type == 'standard':
            standard += 1
            current_tickets += 1
        elif ticket_type == 'kid':
            kid += 1
            current_tickets += 1
        elif ticket_type == 'student':
            student += 1
            current_tickets += 1
    print(f'{name} - {current_tickets / capacity * 100:.2f}% full.')
    name = input()

total = student + kid + standard
print(f'Total tickets: {total}')
print(f'{student / total * 100:.2f}% student tickets.')
print(f'{standard / total * 100:.2f}% standard tickets.')
print(f'{kid / total * 100:.2f}% kids tickets.')

