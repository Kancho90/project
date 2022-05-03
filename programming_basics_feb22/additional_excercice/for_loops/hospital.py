n = int(input())

doctors = 7
treated_patients = 0
untreated = 0

for i in range(1, n + 1):
    patients = int(input())
    if i % 3 == 0 and treated_patients < untreated:
        doctors += 1
    if patients <= doctors:
        treated_patients += patients
    else:
        untreated += patients - doctors
        treated_patients += patients - (patients - doctors)


print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated}.')