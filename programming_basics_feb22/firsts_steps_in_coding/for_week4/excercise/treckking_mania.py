groups = int(input())
musala = 0
montblanc = 0
kilimajaro = 0
k2 = 0
everest = 0
total = 0
for i in range(groups):
    people = int(input())
    total += people
    if people <= 5:
        musala += people
    elif 5 < people <= 12:
        montblanc += people
    elif 12 < people <= 25:
        kilimajaro += people
    elif 25 < people <= 40:
        k2 += people
    else:
        everest += people

print(f'{musala / total * 100:.2f}%')
print(f'{montblanc / total * 100:.2f}%')
print(f'{kilimajaro / total * 100:.2f}%')
print(f'{k2 / total * 100:.2f}%')
print(f'{everest / total * 100:.2f}%')
