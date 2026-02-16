class PaymentSource:
    def pay(self): pass

class Card(PaymentSource):
    def pay(self): print("Paid using Card")

class UPI(PaymentSource):
    def pay(self): print("Paid using UPI")

w = UPI()
w.pay()
