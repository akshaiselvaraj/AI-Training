class Patient:
    def __init__(self, name):
        self.name = name
        
    def treatment_cost(self):
        pass

class GeneralPatient(Patient):
    def treatment_cost(self):
        return 500

class CriticalPatient(Patient):
    def treatment_cost(self):
        return 200

p = CriticalPatient("Rahul")
print("Treatment Cost:", p.treatment_cost())
