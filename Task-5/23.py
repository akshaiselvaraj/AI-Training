class Attendance:
    def record(self): pass

class Manual(Attendance):
    def record(self): print("Attendance taken manually")

class FaceRecognition(Attendance):
    def record(self): print("Attendance via face recognition")

a = FaceRecognition()
a.record()
