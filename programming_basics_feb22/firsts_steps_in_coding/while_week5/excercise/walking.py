steps = 0

while steps < 10000:
    walked = input()

    if walked == 'Going home':
        walked = input()
        steps += int(walked)
        break

    steps += int(walked)

diff = abs(10000 - steps)
if steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')