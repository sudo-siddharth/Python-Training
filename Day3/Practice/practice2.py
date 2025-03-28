# try and catch

try:
    print(x)
except:
    print("An exception occurred")

# try and catch examples , nested try
try:
    print(x)
    try:
        print(y)
    except:
        print("An exception occurred")
except:
    print("An exception occurred")
finally:
    print("Finally block executed")

#Typerror
x="name"
try:
    print(x+2)
except TypeError:
    print("Type error occurred")

# out of bound exception
x=[1,2,3]
try:
    print(x[4])
except IndexError as e:
    print("error: ", e)
finally:
    print("Finally block executed")

# check age example and valuerror using try and catch
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You must be 18 or older to study Python")
    print("Age is:", age)
except ValueError as e:
    print(e)
finally:
    print("Your age is checked.")


    