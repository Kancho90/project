yearly_tax = int(input())
shoes = yearly_tax * 0.6
shorts = shoes * 0.8
ball = shorts * 0.25
accessories = ball * 0.2
total = yearly_tax + shoes + ball + shorts + accessories
formatted_total = '{:.2f}'.format(total)
print(formatted_total)
