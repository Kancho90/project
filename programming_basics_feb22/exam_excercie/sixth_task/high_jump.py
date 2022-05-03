target = int(input())
current_target = target - 30
total_jumps = 0
failed_jumps = 0

while True:
    current_jump = int(input())
    total_jumps += 1
    if current_jump > current_target:
        failed_jumps = 0
        if current_target >= target:
            break
        current_target += 5
    else:
        failed_jumps += 1

    if failed_jumps == 3:
        break

if failed_jumps == 3:
    print(f'Tihomir failed at {current_target}cm after {total_jumps} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {current_target}cm after {total_jumps} jumps.')