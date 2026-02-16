class Package:
    def status(self): pass

class StandardDelivery(Package):
    def status(self): return "Delivered in 5 days"

class ExpressDelivery(Package):
    def status(self): return "Delivered in 2 days"

d = ExpressDelivery()
print(d.status())
