condition = True
prime_sum = 0
non_prime_sum = 0

while condition:

    number = input()
    if number == 'stop':
        condition =  False
        break

    if int(number) < 0:
        print(f'Number is negative.')
    elif int(number) == 0 or int(number) == 1:
        continue
    else:
        non_prime = False
        for i in range(2, int(number)):
            if int(number) % i == 0:
                non_prime = True
        if non_prime:
            non_prime_sum += int(number)
        else:
             prime_sum += int(number)

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')