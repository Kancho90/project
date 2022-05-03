n = int(input())

total_litres = 0
total_degrees = 0

for days in range(n):
    l = float(input())
    total_litres += l
    degrees = float(input())
    total_degrees += degrees * l

avg_degrees = total_degrees / total_litres
print(f'Liter: {total_litres:.2f}')
print(f'Degrees: {avg_degrees:.2f}')
if avg_degrees < 38:
    print(f'Not good, you should baking!')
elif 38 <= avg_degrees <= 42:
    print(f'Super!')
else:
    print('Dilution with distilled water!')