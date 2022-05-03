import math
from math import ceil

height = int(input())
width = int(input())
size = height * width * 4
percent = int(input())
no_paint_area = size * percent / 100
area_to_paint = int(math.ceil(size - no_paint_area))

area_covered = 0
liters = input()

while liters != 'Tired!':
    area_covered += int(liters)
    if area_covered >= area_to_paint:
        break
    liters = input()

diff = abs(area_covered - area_to_paint)
if area_covered == area_to_paint:
    print(f'All walls are painted! Great job, Pesho!')
elif area_covered > area_to_paint:
    print(f'All walls are painted and you have {diff:.0f} l paint left!')
elif area_covered < area_to_paint:
    print(f'{diff:.0f} quadratic m left.')