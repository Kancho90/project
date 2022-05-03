country = input()
sport = input()

total_points = 1

if country == 'Russia':
    if sport == 'ribbon':
        total_points = 9.100 + 9.4
    elif sport == 'hoop':
        total_points = 9.3 + 9.8
    elif sport == 'rope':
        total_points = 9.6 + 9
elif country == 'Bulgaria':
    if sport == 'ribbon':
        total_points = 9.600 + 9.4
    elif sport == 'hoop':
        total_points = 9.55 + 9.75
    elif sport == 'rope':
        total_points = 9.5 + 9.4
elif country == 'Italy':
    if sport == 'ribbon':
        total_points = 9.200 + 9.5
    elif sport == 'hoop':
        total_points = 9.45 + 9.35
    elif sport == 'rope':
        total_points = 9.7 + 9.15

points_left = 20 - total_points
points_percentage = points_left / 20 * 100

print(f'The team of {country} get {total_points:.3f} on {sport}.')
print(f'{points_percentage:.2f}%')