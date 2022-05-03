import math

hours_needed = int(input())
days_available = int(input())
overtime = int(input())

days_total = days_available * 0.9
hours_standard = days_total * 8
hours_overtime = overtime *  2 * days_available
total_workhours = math.floor(hours_overtime + hours_standard)

if total_workhours >= hours_needed:
    hours_left = total_workhours - hours_needed
    print(f'Yes!{hours_left} hours left.')
else:
    hours_remaining = hours_needed - total_workhours
    print(f'Not enough time!{hours_remaining} hours needed.')

