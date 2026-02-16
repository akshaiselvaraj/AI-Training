class Ticket:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def fare(self): pass

class Bus(Ticket):
    def fare(self): return 100

class Train(Ticket):
    def fare(self): return 200

t = Train("A", "B")
print("Fare:", t.fare())
