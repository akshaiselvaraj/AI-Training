class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self): pass

class Warrior(Character):
    def attack(self):
        print("Sword attack!")

class Mage(Character):
    def attack(self):
        print("Magic attack!")

c = Mage(100, 50)
c.attack()
