budget = float(input())
season = input()

destination = ''
spent = budget
type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        type = 'Camp'
        spent = budget * 0.3
    elif season == 'winter':
        type = 'Hotel'
        spent = budget * 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        type = 'Camp'
        spent = budget * 0.4
    elif season == 'winter':
        type = 'Hotel'
        spent = budget * 0.8
else:
    destination = 'Europe'
    type = 'Hotel'
    spent = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{type} - {spent:.2f}')