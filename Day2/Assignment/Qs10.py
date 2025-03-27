class Employee:
    def __init__(self, name: str, employee_id: int, job_type: str, hourly_rate: float, hours_worked: int = 0):
        self.name = name
        self.employee_id = employee_id
        self.job_type = job_type.lower()
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def __str__(self):
        return f"employee: {self.name} (ID: {self.employee_id}) - job type: {self.job_type}"
    
    def calculate_salary(self):
        if self.job_type == "full-time":
            return self.hourly_rate * 40
        elif self.job_type in ("part-time", "contract"):
            return self.hourly_rate * self.hours_worked
        else:
            return 0  # if unknown job type


class Payroll:
    def __init__(self):
        self.employees = []
    
    def add_employee(self,employee: Employee):
        self.employees.append(employee)
    
    def generate_payroll(self):
        print("\nPayroll Report:")
        for i, employee in enumerate(self.employees, 1):
            salary = employee.calculate_salary()
            print(f"{i}. {employee} - salary: ${salary:.2f}")


def get_employee_input():
    print("\nenter Employee details:")
    name = input("Name: ")
    employee_id = int(input("employee ID: "))
    
    while True:
        job_type = input("job type (full-time/part-time/contract): ").lower()
        if job_type in ("full-time", "part-time", "contract"):
            break
        print("invalid job type. please enter full-time, part-time or contract.")
    
    hourly_rate = float(input("hourly Rate: "))
    
    hours_worked = 0
    if job_type in ("part-time", "contract"):
        hours_worked = int(input("Hours Worked: "))
    
    return Employee(name, employee_id, job_type, hourly_rate, hours_worked)


# the main program
payroll = Payroll()

while True:
    payroll.add_employee(get_employee_input())
    more = input("\nAdd another employee? (yes/no): ").lower()
    if more != 'yes':
        break

payroll.generate_payroll()