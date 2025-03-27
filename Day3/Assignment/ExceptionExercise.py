import re

def validate_inputs():
    username = input("Enter the Username (Letters & Numbers only): ")
    if not re.fullmatch(r'^[A-Za-z0-9]+$', username):
        return "Invalid Username"
    
    email = input("Enter email: ")
    if not re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid Email"
    
    age = input("Enter age: ")
    if not re.fullmatch(r'^[1-9]\d*$', age):
        return "Invalid Age"
    
    return f"Registration successful for {username}!"

try:
    result = validate_inputs()
    if "Invalid" in result:
        raise ValueError(result)
    print(result)
except ValueError as e:
    print(f"Error: {e}")