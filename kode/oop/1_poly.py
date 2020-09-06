class Vehicle:
        def __init__(self, model):
            self.model = model

        def vehicle_model(self):
            print(f"Vehicle Model name is {self.model}")

class Bike(Vehicle):
    def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")

class Car(Vehicle):
    def vehicle_model(self):
        print(f"Vehicle name is {self.model}")



ducati = Bike("Ducati=Scrambler")
beetle = Car("Volkswagon-Beetle")

ducati.vehicle_model()
beetle.vehicle_model()


