employees = [
    {"dept_no": 101, "emp_roll": 1, "salary": 50000},
    {"dept_no": 101, "emp_roll": 2, "salary": 60000},
    {"dept_no": 102, "emp_roll": 3, "salary": 45000},
    {"dept_no": 102, "emp_roll": 4, "salary": 70000},
    {"dept_no": 103, "emp_roll": 5, "salary": 55000},
    {"dept_no": 101, "emp_roll": 6, "salary": 52000},
    {"dept_no": 103, "emp_roll": 7, "salary": 65000}
]
dept_salaries = []
for emp in employees:
    dept = emp["dept no"]
    salary = emp["salary"]
    if dept not in dept_salaries:
        dept_salaries[dept] = []

    else:
        dept_salaries[dept].append(salary)

        for dept , salaries in dept_salaries.items():
            print(f"Department{dept}: Min Salary: {min(salaries)} , Max Salary: {max(salaries)}")
            