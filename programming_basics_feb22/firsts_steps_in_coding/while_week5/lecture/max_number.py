from sys import maxsize

max = -sys.maxsize
command = input()

while command != 'Stop':
    number = int(commande)
    if number > max:
        max = number
    commande = input()

print(max)