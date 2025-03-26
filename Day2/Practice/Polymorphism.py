# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c

# calc = Calculator()
# print(calc.add(5, 10))    
# print(calc.add(5, 10, 15)) 


class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

class Sanketh:
    def speak(self):
        return "Scam 1992 BGM"

def make_animal_speak(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()
sanky = Sanketh()

make_animal_speak(cat)
make_animal_speak(dog)
make_animal_speak(sanky)

