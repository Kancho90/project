capacity = int(input())

guests = 0
total = 0
while True:
    new_people = input()

    if new_people == 'Movie time!':
        diff = capacity - guests
        print(f'There are {diff} seats left in the cinema.')
        break

    guests += int(new_people)

    if capacity < guests:
        print('The cinema is full.')
        guests -= int(new_people)
        break


    if int(new_people) % 3 == 0:
        total += int(new_people) * 5 - 5
    else:
        total += int(new_people) * 5

print(f'Cinema income - {total} lv.')
