name1 = input()
name2 = input()

points1 = 0
points2 = 0
winner = ''
points_winner = 0
while True:
    card1 = input()
    if card1 == 'End of game':
        print(f'{name1} has {points1} points')
        print(f'{name2} has {points2} points')
        break
    card2 = input()



    if int(card1) > int(card2):
        points1 += int(card1) - int(card2)
    elif int(card2) > int(card1):
        points2 += int(card2) - int(card1)
    else:
        card1p = int(input())
        card2p = int(input())
        if card1p > card2p:
            winner = name1
            points_winner = points1
        else:
            winner = name2
            points_winner = points2
        print(f'Number wars!')
        print(f'{winner} is winner with {points_winner} points')
        break


