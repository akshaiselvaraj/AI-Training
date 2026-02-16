class Bill:
    def __init__(self, units):
        self.units = units
    def calculate(self):
        pass

class ElectricityBill(Bill):
    def calculate(self):
        return self.units * 5

class WaterBill(Bill):
    def calculate(self):
        return self.units * 2

b = ElectricityBill(100)
print("Bill Amount:", b.calculate())
