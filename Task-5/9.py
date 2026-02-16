class Student:
    def __init__(self, name):
        self.name = name
        self.courses = set()

    def register(self, course):
        if course in self.courses:
            print("Already registered!")
        else:
            self.courses.add(course)
            print("Registered successfully.")

s = Student("Akshai")

s.register("AI")
s.register("ML")
s.register("AI")   # duplicate
print("Courses:", s.courses)
