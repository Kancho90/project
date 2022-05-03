eggs1 = int(input())
eggs2 = int(input())

while True:
    text = input()

    if text == 'End of battle':
        print(f'Player one has {eggs1} eggs left.')
        print(f'Player two has {eggs2} eggs left.')
        break

    if text == 'one':
        eggs2 -= 1
    elif text == 'two':
        eggs1 -= 1

    if eggs1 == 0:
        print(f'Player one is out of eggs. Player two has {eggs2} eggs left.')
        break
    if eggs2 == 0:
        print(f'Player two is out of eggs. Player one has {eggs1} eggs left.')
        break
