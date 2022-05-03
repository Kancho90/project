eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0

for i in range(eggs):
    color = input()
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1

max = red
max_color = 'red'
if orange > max:
    max = orange
    max_color = 'orange'
if blue > max:
    max = blue
    max_color = 'blue'
if green > max:
    max = green
    max_color = 'green'

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max} -> {max_color}')
