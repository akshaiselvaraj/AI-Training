class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        pass

class RegularGrading(Student):
    def grade(self):
        return "A" if self.marks >= 80 else "B"

class LenientGrading(Student):
    def grade(self):
        return "A" if self.marks >= 70 else "B"

s = LenientGrading("Akshai", 75)
print("Grade:", s.grade())
