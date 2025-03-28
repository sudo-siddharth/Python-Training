import re

EMAIL_REGEX = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

try:
    with open(r'Day3\Assignment\Data_files\contacts.txt') as f:
        content = f.read()
        emails = EMAIL_REGEX.findall(content)
        if emails:
            print('\n'.join(emails))
        else:
            print("No valid emails found")
except FileNotFoundError:
    print("Error: contacts.txt not found")
except Exception as e:
    print(f"An error occurred: {e}")