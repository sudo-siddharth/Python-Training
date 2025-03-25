
students = {
    "student1": {
        "name": "Siddharth",
        "college": "xyz college",
        "roll_no": 101,
        "marks": 85
    },
    "student2": {
        "name": "Sanketh",
        "college": "Reyansh College",
        "roll_no": 102,
        "marks": 12
    }
}

#access marks of second student
print(students["student2"]["marks"])

#looping using items method for the student dictionary
for key, value in students.items():
    print(key, value)

# looping using value method for the student dictionary
for value in students.values():
    print(value)
