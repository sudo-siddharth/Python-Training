import re
import csv

class InvalidAgeException(Exception):
    pass

EMAIL_REGEX = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')

try:
    with open(r'Day3\Assignment\Data_files\users.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                age = int(row['Age'])
                if age < 18:
                    raise InvalidAgeException(f"Invalid Age: {row['Name']} ({row['Age']})")
                
                if not EMAIL_REGEX.fullmatch(row['Email']):
                    print(f"Invalid Email: {row['Name']} - {row['Email']}")
                    continue
                    
                print(f"Valid User: {row['Name']} ({age}) - {row['Email']}")
                
            except ValueError:
                print(f"Invalid Age Format: {row['Name']} ({row['Age']})")
            except InvalidAgeException as e:
                print(e)
                
except FileNotFoundError:
    print("Error: users.csv not found")
except Exception as e:
    print(f"An error occurred: {e}")