customers = int(input())
total_spent = 0

for i in range(customers):
    items_bought = 0
    current_total = 0

    item = input()

    while True:

        if item == 'Finish':
            if items_bought % 2 == 0:
                current_total *= 0.8
            print(f'You purchased {items_bought} items for {current_total:.2f} leva.')
            total_spent += current_total
            break

        if item == 'basket':
            current_total += 1.5
            items_bought += 1
        elif item == 'wreath':
            current_total += 3.8
            items_bought += 1
        elif item == 'chocolate bunny':
            current_total += 7
            items_bought += 1

        item = input()

print(f'Average bill per client is: {total_spent / customers:.2f} leva.')