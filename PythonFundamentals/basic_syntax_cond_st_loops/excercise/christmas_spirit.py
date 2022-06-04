quantity = int(input())
days = int(input())

spent = 0
spirit = 0

for i in range (1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        spirit += 5
        spent += quantity * 2
    if i % 3 == 0:
        spirit += 13
        spent += quantity * 8
    if i % 5 == 0:
        if i % 3 == 0:
            spirit += 30
        spirit += 17
        spent += quantity * 15
    if i % 10 == 0:
        spirit -= 20
        spent += 23

if days % 10 == 0:
    spirit -= 30

print(f'Total cost: {spent}')
print(f'Total spirit: {spirit}')
