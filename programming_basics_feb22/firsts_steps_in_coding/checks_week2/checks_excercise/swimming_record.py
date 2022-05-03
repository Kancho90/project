import math

record_in_seconds = float(input())
meters = float(input())
time_for_1m_in_seconds = float(input())

additional_time = math.floor(meters / 15) * 12.5
time_needed_to_finish = (meters * time_for_1m_in_seconds) + additional_time
comparison_to_wr = record_in_seconds -  time_needed_to_finish
time_left = time_needed_to_finish - record_in_seconds

if comparison_to_wr > 0:
    print(f'Yes, he succeeded! The new world record is {time_needed_to_finish:.2f} seconds.')
elif comparison_to_wr <= 0:
    print(f'No, he failed! He was {time_left:.2f} seconds slower.')
