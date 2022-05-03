free_days = int(input())

working_days = 365 - free_days

play_workdays = working_days * 63
play_free = free_days * 127

play_limit = 30000
total_play = play_free + play_workdays

overtime = total_play - play_limit
overtime_h = overtime // 60
overtime_m = overtime % 60

undertime = play_limit - total_play
undertime_h = undertime // 60
undertime_m = undertime % 60

if total_play > play_limit:
    print('Tom will run away')
    print(f'{overtime_h} hours and {overtime_m} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{undertime_h} hours and {undertime_m} minutes less for play')