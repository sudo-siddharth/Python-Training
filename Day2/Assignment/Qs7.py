class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def __str__(self):
        return f"Student: {self.name} (Roll No: {self.roll_number}), Marks: {self.marks}"

name = input("enter student name: ")
roll_number = int(input("enter roll number: "))
marks = float(input("enter marks: "))

student = Student(name, roll_number, marks)

print(student)