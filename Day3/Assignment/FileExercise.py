import csv

with open('Day3\Assignment\Data_files\employees.csv') as f:
    for line in f:
        print(line.strip())

id = input("\nEnter employee ID: ")
with open('Day3\Assignment\Data_files\employees.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['ID'] == id:
            print(row)
            break
    else:
        print("Employee not found")