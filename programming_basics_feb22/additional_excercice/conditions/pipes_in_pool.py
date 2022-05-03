import math

v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_total = p1 * h
p2_total = p2 * h

total_l = p1_total + p2_total
overflow = total_l - v

if total_l <= v:
    pipe1 = p1_total / total_l * 100
    pipe2 = p2_total / total_l * 100
    fill_percentage = total_l / v * 100
    print(f'The pool is {fill_percentage:.2f}% full. Pipe 1: {pipe1:.2f}%. Pipe 2: {pipe2:.2f}%.')
else:
    print(f'For {h} hours the pool overflows with {overflow} liters.')
