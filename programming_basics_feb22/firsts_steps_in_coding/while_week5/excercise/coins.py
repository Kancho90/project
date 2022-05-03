difference = int(float(input()) * 100)
coins = 0

while difference > 0:

    if difference >= 200:
        difference -= 200
    elif difference >= 100:
        difference -= 100
    elif difference >= 50:
        difference -= 50
    elif difference >= 20:
        difference -= 20
    elif difference >= 10:
        difference -= 10
    elif difference >= 5:
        difference -= 5
    elif difference >= 2:
        difference -= 2
    elif difference >= 1:
        difference -= 1

    coins += 1

print(coins)