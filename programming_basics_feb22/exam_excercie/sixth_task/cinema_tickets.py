student_tickets = 0
kids_tickets = 0
standard_tickets = 0

name = input()

while name != 'Finish':
    seats = int(input())
    current_seats = 0
    type = ''

    while current_seats < seats and type != 'End':
        type = input()

        if type == 'student':
            student_tickets += 1
            current_seats += 1
        elif type == 'standard':
            standard_tickets += 1
            current_seats += 1
        elif type == 'kid':
            kids_tickets += 1
            current_seats += 1

    print(f'{name} - {current_seats / seats * 100:.2f}% full.')
    name = input()




total = student_tickets + standard_tickets + kids_tickets
print(f'Total tickets: {total}')
print(f'{student_tickets / total * 100:.2f}% student tickets.')
print(f'{standard_tickets / total * 100:.2f}% standard tickets.')
print(f'{kids_tickets / total * 100:.2f}% kids tickets.')