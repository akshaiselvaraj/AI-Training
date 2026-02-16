class Inference:
    def run(self): pass

class RuleBased(Inference):
    def run(self): return "Rule-based result"

class MLBased(Inference):
    def run(self): return "ML-based result"

i = MLBased()
print(i.run())
