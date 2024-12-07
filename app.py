class Smartphone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def get_details(self):
        return f"{self.brand} {self.model}, Price: ${self.price}, Storage: {self.storage}GB"

    def make_call(self, number):
        return f"Dialing {number} from {self.brand} {self.model}..."

    def browse_internet(self):
        return f"Browsing internet on {self.brand} {self.model}..."

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, storage, cooling_system):
        super().__init__(brand, model, price, storage)
        self.cooling_system = cooling_system

    def game_mode(self):
        return f"Activating game mode with {self.cooling_system} cooling system!"

class BusinessSmartphone(Smartphone):
    def __init__(self, brand, model, price, storage, encryption_level):
        super().__init__(brand, model, price, storage)
        self.encryption_level = encryption_level

    def secure_email(self):
        return f"Sending a secure email with {self.encryption_level} encryption."

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(vehicle.move())

if __name__ == "__main__":
    print("=== Activity 1: Smartphones ===")
    iphone = Smartphone("Apple", "iPhone 15", 999, 256)
    asus_rog = GamingSmartphone("Asus", "ROG Phone 6", 1199, 512, "Liquid cooling")
    blackberry = BusinessSmartphone("BlackBerry", "Key3", 699, 128, "AES-256")

    print(iphone.get_details())
    print(asus_rog.game_mode())
    print(blackberry.secure_email())

    print("\n=== Activity 2: Vehicle Movements ===")
    car = Car()
    plane = Plane()
    boat = Boat()
    bicycle = Bicycle()

    vehicles = [car, plane, boat, bicycle]
    demonstrate_movement(vehicles)

