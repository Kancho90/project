actor = input()
points_academy = float(input())
n = int(input())

for i in range(n):
    name = input()
    points = float(input())
    points_academy += (len(name) * points /2)
    if points_academy > 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {points_academy:.1f}!')
        break

if points_academy <= 1250.5:
    needed_points = 1250.5 - points_academy
    print(f'Sorry, {actor} you need {needed_points:.1f} more!')