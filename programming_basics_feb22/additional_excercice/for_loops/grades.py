students = int(input())

fail = 0
d = 0
c = 0
top = 0
total_grades = 0

for i in range(students):
    grade = float(input())
    total_grades += grade
    if grade < 3:
        fail += 1
    elif 3 <= grade <4:
        d += 1
    elif 4 <= grade < 5:
        c += 1
    else:
        top += 1

print(f'Top students: {top/students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {c/students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {d/students * 100:.2f}%')
print(f'Fail: {fail/students * 100:.2f}%')
print(f'Average: {total_grades/students:.2f}')