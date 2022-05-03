vaucher = int(input())

tickets_bought = 0
other_items = 0

while True:
    item = input()
    if item == 'End':
        break
    if len(item) > 8:
        price = ord(item[1]) + ord(item[0])
        if price > vaucher:
            break
        else:
            vaucher -= price
            tickets_bought += 1
    else:
        price = ord(item[0])
        if price > vaucher:
            break
        else:
            vaucher -= price
            other_items += 1

print(tickets_bought)
print(other_items)
