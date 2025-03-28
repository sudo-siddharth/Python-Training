class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def show_details(self):
        super().show_details()
        print(f"Seats: {self.seats}")


car = Car("Toyota", "Corolla", 5)
car.show_details()