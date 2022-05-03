import math

record = float(input())
distance = float(input())
time_for1m = float(input())

added_time = math.floor(distance / 50) * 30
total_time = distance * time_for1m + added_time

if total_time < record:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    time_needed = total_time - record
    print(f'No! He was {time_needed:.2f} seconds slower.')