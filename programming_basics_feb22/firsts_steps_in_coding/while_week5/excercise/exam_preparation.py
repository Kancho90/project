bad_results = int(input())
poor_grades = 0
problems_solved = 0
last_name = ''
average_grade = 0


while True:
    name = input()
    if name == 'Enough':
        average_grade /= problems_solved
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {problems_solved}')
        print(f'Last problem: {last_name}')
        break
    grade = int(input())
    if grade <= 4:
        poor_grades += 1
    if poor_grades == bad_results:
        print(f'You need a break, {poor_grades} poor grades.')
        break
    last_name = name
    problems_solved += 1
    average_grade += grade



