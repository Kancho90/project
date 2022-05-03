trunk_volume = float(input())

loaded_suitcases = 0
loaded_volume = 0

while True:
    suitcase_volume = input()

    if suitcase_volume == 'End':
        print('Congratulations! All suitcases are loaded!')
        break

    loaded_suitcases += 1
    if loaded_suitcases % 3 == 0:
        loaded_volume += float(suitcase_volume) * 1.1
    else:
        loaded_volume += float(suitcase_volume)

    if loaded_volume > trunk_volume:
        loaded_suitcases -= 1
        print(f'No more space!')
        break

print(f'Statistic: {loaded_suitcases} suitcases loaded.')