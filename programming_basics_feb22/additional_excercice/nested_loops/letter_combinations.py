first = input()
second = input()
skip = input()
combinations = 0
for letter1 in range(ord(first), ord(second) + 1):
    if letter1 != ord(skip):
        print1 = chr(letter1)
        for letter2 in range(ord(first), ord(second) + 1):
            if letter2 != ord(skip):
                print2 = chr(letter2)
                for letter3 in range(ord(first), ord(second) + 1):
                    if letter3 != ord(skip):
                        print3 = chr(letter3)
                        print(f'{print1}{print2}{print3}', end=' ')
                        combinations += 1
print(f'{combinations}')