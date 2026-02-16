class Exam:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

    def evaluate(self): pass

class ObjectiveExam(Exam):
    def evaluate(self):
        return self.marks

class PracticalExam(Exam):
    def evaluate(self):
        return self.marks + 5

e = PracticalExam("AI", 80)
print("Final Marks:", e.evaluate())
