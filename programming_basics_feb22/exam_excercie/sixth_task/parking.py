number_of_days = int(input())
hours = int(input())
total_parking = 0

for i in range(1, number_of_days + 1):

    day_fee = 0
    for h in range(1, hours + 1):
        if i % 2 ==0:
            if h % 2 != 0:
                day_fee += 2.5
            else:
                day_fee += 1
        else:
            if h % 2 == 0:
                day_fee += 1.25
            else:
                day_fee += 1
    print(f'Day: {i} - {day_fee:.2f} leva')
    total_parking += day_fee

print(f'Total: {total_parking:.2f} leva')
