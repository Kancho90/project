width = int(input())
height = int(input())

number_of_pieces = width * height
pieces_eaten = 0

while pieces_eaten < number_of_pieces:
    piece = input()

    if piece == 'STOP':
        break

    pieces_eaten += int(piece)

diff = abs(number_of_pieces - pieces_eaten)
if number_of_pieces >= pieces_eaten:
    print(f'{diff:.0f} pieces are left.')
else:
    print(f'No more cake left! You need {diff:.0f} pieces more.')