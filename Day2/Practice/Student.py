class Student:
    def __init__(self, USN, name, Branch, Phone):
        self.USN = USN
        self.name = name
        self.Branch = Branch
        self.Phone = Phone

    def display_details(self):
        print(f"USN = {self.USN}, name = {self.name}, branch = {self.Branch}, phone = {self.Phone}")


n = int(input("Enter number of students: "))
students = []


for i in range(n):
    print("Enter details of Student - ", i+1)
    USN = input("Enter USN: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    phone = input("Enter Phone: ")
    
    student = Student(USN, name, branch, phone)
    students.append(student)

for student in students:
    student.display_details()

  
  