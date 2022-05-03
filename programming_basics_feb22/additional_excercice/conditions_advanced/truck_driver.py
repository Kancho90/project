season =  input()
km_per_month =  float(input())

pay =  1

if km_per_month  <= 5000:
    if season == 'Spring' or season == 'Autumn':
        pay = 0.75
    elif  season == 'Summer':
        pay =  0.9
    else:
        pay = 1.05
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        pay = 0.95
    elif  season == 'Summer':
        pay =  1.1
    else:
        pay = 1.25
else:
    pay = 1.45

total_pay = (pay * km_per_month * 4) * 0.9
print(f'{total_pay:.2f}')
