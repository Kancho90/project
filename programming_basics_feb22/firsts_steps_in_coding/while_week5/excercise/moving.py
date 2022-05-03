h = int(input())
w = int(input())
l = int(input())

size = h * w * l
current_size = 0

while current_size < size:
    box = input()

    if box == 'Done':
        break

    current_size += int(box)

diff = abs(size -  current_size)
if size >= current_size:
    print(f'{diff} Cubic meters left.')
else:
    print(f'No more free space! You need {diff} Cubic meters more.')