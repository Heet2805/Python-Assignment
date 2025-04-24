# Create a dictionary in python with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.

dict1 = {
    'dept1': {'roll_no': 101, 'salary': 50000},
    'dept2': {'roll_no': 102, 'salary': 60000},
    'dept3': {'roll_no': 103, 'salary': 55000},
}


def find_min_max_salary(dept_dict):
    min_salary = float('inf')
    max_salary = float('-inf')
    for dept, info in dept_dict.items():
        salary = info['salary']
        if salary < min_salary:
            min_salary = salary
        if salary > max_salary:
            max_salary = salary
    return min_salary, max_salary


min_salary, max_salary = find_min_max_salary(dict1)
print(f"Minimum Salary: {min_salary}")
print(f"Maximum Salary: {max_salary}")
