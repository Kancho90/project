season  = input()
group =  input()
number_of_students = int(input())
number_of_nights = int(input())

price = 1
sport = ''

if season == 'Winter':
    if group == 'boys' or group == 'girls':
        price = 9.6
    else:
        price = 10
elif season == 'Spring':
    if group == 'boys' or group == 'girls':
        price = 7.2
    else:
        price = 9.5
else:
    if group == 'boys' or group == 'girls':
        price = 15
    else:
        price = 20

if group == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    else:
        sport = 'Volleyball'
elif group == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    else:
        sport = 'Football'
else:
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    else:
        sport = 'Swimming'

total = number_of_nights * number_of_students * price

if number_of_students >= 50:
    total = total * 0.5
elif 20 <= number_of_students < 50:
    total = total * 0.85
elif 20 > number_of_students >= 10:
    total = total * 0.95

print(f'{sport} {total:.2f} lv.')