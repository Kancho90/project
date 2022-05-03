n1 = int(input())
m1 = int(input())
n2 = int(input())
m2 = int(input())

e1 = n1 + n2
e2 = m1 + m2

for i1 in range (n1, e1 + 1):
    nonprime1 = True
    for primecheck1 in range(2, i1):
        if i1 % primecheck1 == 0:
            nonprime1 = False
    if nonprime1:
        for i3 in range(m1, e2 + 1):
            nonprime2 = True
            for primechec2 in range(2, i3):
                if i3 % primechec2 ==0:
                    nonprime2 = False
            if nonprime2:
                print(f'{i1}{i3}')