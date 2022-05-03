jury = int(input())
condition = True
number_of_presentations = 0
total_grade = 0
while True:
    name = input()
    current_grade = 0
    if name == 'Finish':
        condition = False
        break

    for i in range(jury):
        score = float(input())
        current_grade += score

    print(f'{name} - {current_grade / jury:.2f}.')
    total_grade += current_grade / jury
    number_of_presentations += 1

average_grade = total_grade / number_of_presentations
print(f"Student's final assessment is {average_grade:.2f}.")