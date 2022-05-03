number_tournaments = int(input())

raised_money = 0
total_raised_money = 0
bonus = 0
total_win = 0
total_lose = 0


for current_tournament in range(1, number_tournaments + 1):
    type_sport = input()


    while type_sport != "Finish":
        result = input()
        win_counter = 0
        lose_counter = 0
        if result == "win":
            win_counter += 1
            raised_money += 20
        elif result == "lose":
            lose_counter += 1
        type_sport = input()

    if win_counter > lose_counter:
        bonus = raised_money * 0.10
        raised_money = raised_money + bonus
        total_win  += 1
    else:
        total_lose += 1

    total_raised_money= raised_money

if total_win > total_lose:
    total_raised_money = total_raised_money + total_raised_money * 0.20
    print(f"You won the tournament! Total raised money: {total_raised_money}")
else:
    print(f"You lost the tournament! Total raised money: {total_raised_money}")
