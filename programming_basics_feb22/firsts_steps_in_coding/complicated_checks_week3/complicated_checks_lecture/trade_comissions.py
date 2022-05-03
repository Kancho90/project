city = input()
sales = float(input())
cities = ['Sofia', 'Varna', 'Plovdiv']

if city not in cities or sales < 0:
    print('error')
else:
    comission = 0
    if city == 'Sofia':
        if 0 <= sales <= 500:
            comission = 0.05
        elif 500 < sales <= 1000:
            comission = 0.07
        elif 1000 < sales <= 10000:
            comission = 0.08
        elif sales > 10000:
            comission = 0.12
    elif city == 'Varna':
        if 0 <= sales <= 500:
            comission = 0.045
        elif 500 < sales <= 1000:
            comission = 0.075
        elif 1000 < sales <= 10000:
            comission = 0.1
        elif sales > 10000:
            comission = 0.13
    elif city == 'Plovdiv':
        if 0 <= sales <= 500:
            comission = 0.055
        elif 500 < sales <= 1000:
            comission = 0.08
        elif 1000 < sales <= 10000:
            comission = 0.12
        elif sales > 10000:
            comission = 0.145
    compensation = sales * comission
    print(f'{compensation:.2f}')
