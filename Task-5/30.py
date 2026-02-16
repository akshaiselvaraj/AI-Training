class DriveMode:
    def control(self): pass


class Eco(DriveMode):
    def control(self): print("Eco driving mode")


class Sport(DriveMode):
    def control(self): print("Sport driving mode")


d = Sport()
d.control()
