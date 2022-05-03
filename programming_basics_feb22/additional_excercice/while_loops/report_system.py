sum_to_be_gathered = int(input())

gathered_sum = 0
cc_payments = 0
cash_payments = 0
total_payments = 0
cash_sum = 0
credit_sum = 0

while gathered_sum < sum_to_be_gathered:
    price = input()

    if price == 'End':
        print('Failed to collect required money for charity.')
        break
    total_payments += 1
    if total_payments % 2 != 0:
        if int(price) > 100:
            print(f'Error in transaction!')
        else:
            cash_payments += 1
            gathered_sum += int(price)
            cash_sum += int(price)
            print(f'Product sold!')
    if total_payments % 2 == 0:
        if int(price) < 10:
            print(f'Error in transaction!')
        else:
            cc_payments += 1
            gathered_sum += int(price)
            credit_sum += int(price)
            print(f'Product sold!')

if gathered_sum >= sum_to_be_gathered:
    print(f'Average CS: {cash_sum / cash_payments:.2f}')
    print(f'Average CC: {credit_sum / cc_payments:.2f}')