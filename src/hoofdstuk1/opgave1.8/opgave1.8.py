class Vehicle:
    def __init__(self, brand, max_speed, mileage, seats):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
        self.seats = seats

    def ticket(self):
        price = 5 / self.seats
        return price


class Bus(Vehicle):
    def __init__(self, brand, max_speed, mileage, seats=50):
        super().__init__(brand, max_speed, mileage, seats)
        self.merk = "De Lijn"

    def ticket(self, afstand):
        price = (5 / self.seats) * afstand
        return price
