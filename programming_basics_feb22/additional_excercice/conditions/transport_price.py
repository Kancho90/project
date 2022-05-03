number_of_kms = int(input())
time_of_day = input()

taxi_start = 0.7
taxi_day = 0.79
taxi_night = 0.9

bus_fee = 0.09
train_fee = 0.06

if number_of_kms < 20:
    if time_of_day == 'day':
        price = 0.7 + number_of_kms * taxi_day
    elif time_of_day == 'night':
        price = 0.7 + number_of_kms * taxi_night
    else:
        price = 0 * number_of_kms
elif number_of_kms < 100:
    price = number_of_kms * bus_fee
else:
    price = number_of_kms * train_fee

print(f'{price:.2f}')