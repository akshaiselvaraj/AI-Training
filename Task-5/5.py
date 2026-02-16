# Base Class
class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} Car is driving smoothly on the road using {self.fuel_type}.")

class Bike(Vehicle):
    def drive(self):
        print(f"{self.brand} Bike is riding fast using {self.fuel_type}.")

class Truck(Vehicle):
    def drive(self):
        print(f"{self.brand} Truck is carrying heavy loads using {self.fuel_type}.")

print("1. Car")
print("2. Bike")
print("3. Truck")
choice = int(input("Choose vehicle type: "))
brand = input("Enter brand: ")
fuel = input("Enter fuel type: ")

if choice == 1:
    v = Car(brand, fuel)
elif choice == 2:
    v = Bike(brand, fuel)
elif choice == 3:
    v = Truck(brand, fuel)
else:
    print("Invalid choice")
    exit()
v.drive()
