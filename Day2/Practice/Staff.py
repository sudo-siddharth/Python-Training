class Staff:
    def __init__(self, staffID, name, phone, salary):
        self.staffID = staffID
        self.name = name
        self.phone = phone
        self.salary = salary

    def display_details(self):
        print(f"staff ID = {self.staffID}, name = {self.name}, phone = {self.phone}, salary = {self.salary}")

class Teaching(Staff):
    def __init__(self, staffID, name, phone, salary, domain, publication):
        super().__init__(staffID, name, phone, salary)
        self.domain=domain
        self.publication=publication

    def display_details(self):
        super().display_details()
        print(f"domain = {self.domain}, publication = {self.publication}")

class Technical(Staff):
    def __init__(self, staffID,name,phone,salary,skills):
        super().__init__(staffID,name,phone,salary)
        self.skills=skills

    def display_details(self):
        super().display_details()  

        print(f"skills = {self.skills}")

class Contact(Staff):
    def __init__(self,staffID,name,phone,salary,period):
        super().__init__(staffID,name,phone,salary)
        self.period=period

    def display_details(self):
        super().display_details()
        print(f"period = {self.period}")


n = int(input("enter number of staffs = "))
staffs = []

for i in range(n):
    print("enter details of Staff - ", i+1)
    staffID = input("Enter staff ID: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    salary = input("Enter Salary: ")
    staff_type = input("Enter staff type (teaching/technical/contact): ")

    if staff_type == "teaching":
        domain = input("Enter domain: ")
        publication = input("Enter publication: ")
        staff = Teaching(staffID, name, phone, salary, domain, publication)
    elif staff_type == "technical":
        skills = input("Enter skills: ")
        staff = Technical(staffID, name, phone, salary, skills)
    elif staff_type == "contact":
        period = input("Enter period: ")
        staff = Contact(staffID, name, phone, salary, period)
    else:
        staff = Staff(staffID, name, phone, salary)

    staffs.append(staff)

for staff in staffs:
    staff.display_details()

