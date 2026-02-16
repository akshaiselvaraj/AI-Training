class Reservation:
    def check(self): pass

class Normal(Reservation):
    def check(self): return "Table available"

class VIP(Reservation):
    def check(self): return "VIP table reserved"

r = VIP()
print(r.check())
