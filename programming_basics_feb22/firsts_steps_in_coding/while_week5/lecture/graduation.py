    name = input()

    grade_total = 0
    total = 0
    bad_counter = 0
    bad_condition = False

    while grade_total < 12:
        grade =  float(input())

        if grade < 4:
            bad_counter += 1
            if bad_counter > 1:
                bad_condition = True
                grade_total += 1
                break
        else:
            total += grade
            grade_total += 1

    if bad_condition:
        print(f'{name} has been excluded at {grade_total} grade')
    else:
        total /= grade_total
        print(f'{name} graduated. Average grade: {total:.2f}')
