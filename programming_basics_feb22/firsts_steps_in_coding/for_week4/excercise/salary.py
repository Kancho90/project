n = int(input())
salary = int(input())

for test in range(n):
    site =  input()

    if site == 'Facebook':
        salary -= 150
    if site == 'Instagram':
        salary -= 100
    if site == 'Reddit':
        salary -= 50
    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:
    print(salary)