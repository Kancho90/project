n1 = int(input())
n2 = int(input())

n3 = 0
for i in range(0, n2 +1):
    if i % n1 == 0 and i > n3:
        n3 = i

print(n3)