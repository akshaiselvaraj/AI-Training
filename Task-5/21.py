class Plan:
    def bill(self): pass

class BasicPlan(Plan):
    def bill(self): return "₹199 / month"

class PremiumPlan(Plan):
    def bill(self): return "₹499 / month"

p = PremiumPlan()
print("Billing:", p.bill())
