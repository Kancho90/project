n1 = int(input())
n2 = int(input())
n3 = int(input())

for i1 in range(1, n1 + 1):
    if i1 % 2 == 0:
        for i2 in range(2, n2 + 1):
            prime = True
            for check in range (2, i2):
                if i2 % check == 0:
                    prime = False
                    break
            if prime:
                for i3 in range(1, n3 + 1):
                    if i3 % 2 == 0:
                        print(f'{i1} {i2} {i3}')
