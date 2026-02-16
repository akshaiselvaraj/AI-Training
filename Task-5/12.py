class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self): pass

class Veg(Food):
    def final_price(self):
        return self.price * 0.9   # 10% discount

class NonVeg(Food):
    def final_price(self):
        return self.price * 1.1   # 10% extra

f = Veg("Paneer", 200)
print("Bill:", f.final_price())
