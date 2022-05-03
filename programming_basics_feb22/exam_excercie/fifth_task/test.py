luggage_capacity = float(input())
free_space = 0
command = 0
total_luggage = 0
suitcase_counter = 0


while True:
    suitcase_volume = input()

    if suitcase_volume == 'End':
            print('Congratulations! All suitcases are loaded!')
            print(f'Statistic: {suitcase_counter} suitcases loaded.')
            break

    suitcase_counter += 1
    suitcase_volume = float(suitcase_volume)
    if suitcase_counter % 3 == 0:
        suitcase_volume += suitcase_volume * 0.10

    total_luggage += suitcase_volume

    if total_luggage > luggage_capacity:
        suitcase_counter -= 1
        print('No more space!')
        print(f'Statistic: {suitcase_counter} suitcases loaded.')
        break
