students_sold = 0
kids_sold = 0
standard_sold = 0

while True:
    movie = input()
    projection = 0
    if movie == 'Finish':
        break
    seats = int(input())
    while True:
        ticket = input()
        if ticket == 'End' or ticket == 'Finish':
            break
        elif ticket == 'student':
            students_sold += 1
        elif ticket == 'kid':
            kids_sold += 1
        elif ticket == 'standard':
            standard_sold += 1
        projection += 1
        if projection == seats:
            break
    print(f'{movie} - {projection / seats * 100:.2f}% full.')
    if ticket == 'Finish':
         break


total = kids_sold + standard_sold + students_sold
print(f'Total tickets: {total}')
print(f'{students_sold / total * 100:.2f}% student tickets.')
print(f'{standard_sold / total * 100:.2f}% standard tickets.')
print(f'{kids_sold / total * 100:.2f}% kids tickets.')