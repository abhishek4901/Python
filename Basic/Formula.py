basic = float(input("Enter basic salary: "))
grade = input("Enter grade (A/B/Other): ")

if grade == 'A':
    allowance = 1700.0
elif grade == 'B':
    allowance = 1500.0
else:
    allowance = 1300.0

hra = 0.2 * basic
da = 0.5 * basic
pf = 0.11 * basic

gross_salary = round(basic + hra + da + allowance - pf)
print("Gross Salary:", gross_salary)
