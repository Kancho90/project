visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for i in range(visitors):
    activity = input()
    if activity == 'Back':
        back += 1
    elif activity == 'Chest':
        chest += 1
    elif activity == 'Legs':
        legs += 1
    elif activity == 'Abs':
        abs += 1
    elif activity == 'Protein shake':
        protein_shake += 1
    elif activity == 'Protein bar':
        protein_bar += 1

workout = back + chest + legs + abs
buyers = protein_bar + protein_shake

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{workout / visitors * 100:.2f}% - work out')
print(f'{buyers / visitors * 100:.2f}% - protein')
