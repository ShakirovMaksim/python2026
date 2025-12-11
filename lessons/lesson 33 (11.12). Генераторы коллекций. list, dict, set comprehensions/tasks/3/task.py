import math

departments = [
    {
        "name": "Backend",
        "budget": 600000,
        "employees": [
            {"name": "Ann", "salary": 180000, "is_remote": True},
            {"name": "Bob", "salary": 170000, "is_remote": False},
            {"name": "Cara", "salary": 160000, "is_remote": True}
        ]
    },
    {
        "name": "Ops",
        "budget": 250000,
        "employees": [
            {"name": "Dan", "salary": 140000, "is_remote": False},
            {"name": "Eve", "salary": 130000, "is_remote": False}
        ]
    }
]

def total_salary(employees):
    return sum(emp["salary"] for emp in employees)

def avg_salary(employees):
	avg = total_salary(employees) / len(employees)
	return math.ceil(avg)

def remote_percentage(employees):
	remote_amount = len([emp for emp in employees if emp['is_remote'] == True])
	return round(remote_amount / len(employees), 2)

dept_summary = {
    name: (avg_salary(employees), remote_percentage(employees))
    for name, budget, employees in departments
    if len(employees) >= 3 and budget > total_salary(employees)}

print(dept_summary)
