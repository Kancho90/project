n = int(input())

for i in range (n):
    string = input()
    if '_' in string or '.' in string or ',' in string:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
