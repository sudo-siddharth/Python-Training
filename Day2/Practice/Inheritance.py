class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
animal = Animal()
print(dog.sound())
print(animal.sound())


# polymorphism example
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)

# using super keyoword for example
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

dog = Dog("Jacky")
dog.who_am_i()
print("Now printing the dog name:")
print(dog.name)