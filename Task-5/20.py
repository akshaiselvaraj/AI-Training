class Ride:
    def __init__(self, distance):
        self.distance = distance

    def fare(self):
        pass

class MiniRide(Ride):
    def fare(self):
        return self.distance * 10

class PrimeRide(Ride):
    def fare(self):
        return self.distance * 20

r = PrimeRide(5)
print("Fare:", r.fare())
