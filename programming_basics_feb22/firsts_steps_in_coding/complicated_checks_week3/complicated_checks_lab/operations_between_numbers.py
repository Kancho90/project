n1 = int(input())
n2 = int(input())
operator = input()

result = n1 + n2
odd = ''
devision  = ['/', '%']

if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        odd = 'even'
    else:
        odd = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd}')
elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        odd = 'even'
    else:
        odd = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd}')
elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        odd = 'even'
    else:
        odd = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd}')
elif n2 == 0 and operator in devision:
    print(f'Cannot divide {n1} by zero')
elif operator == '/':
    result = n1 / n2
    result = '{:.2f}'.format(result)
    print(f'{n1} / {n2} = {result}')
elif operator == '%':
    result = n1 % n2
    print(f'{n1} % {n2} = {result}')
