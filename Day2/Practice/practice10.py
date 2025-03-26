# class Main:
#     x=10

# print(Main.x)

# __str__ and __init__ examples in python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

person = Person("Sanketh", 30)
print(person)


# without using __str__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
person = Person("Sanketh", 30)
print(person)