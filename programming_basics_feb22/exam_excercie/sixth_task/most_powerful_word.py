import math

winner_word = ''
sum_for_winner = 0

while True:
    word = input()
    current_sum = 0
    if word == 'End of words':
        break

    for i in range(len(word)):
        current_sum += ord(word[i])

    if word[0].upper() in ('A', 'E', 'U', 'O', 'I', 'Y'):
        current_sum *= len(word)
    else:
        current_sum /= len(word)
        current_sum = math.floor(current_sum)

    if current_sum > sum_for_winner:
        sum_for_winner = current_sum
        winner_word = word

print(f'The most powerful word is {winner_word} - {sum_for_winner}')