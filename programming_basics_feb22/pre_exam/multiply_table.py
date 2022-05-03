number = int(input())

n1 = str(number)[2]
n1 = int(n1)
n2 = str(number)[1]
n2 = int(n2)
n3 = str(number)[0]
n3 = int(n3)

for i1 in range(1, n1 + 1):
    for i2 in range(1, n2 + 1):
        for i3 in range(1, n3 + 1):
            result = i1 * i2 * i3
            print(f'{i1} * {i2} * {i3} = {result};')