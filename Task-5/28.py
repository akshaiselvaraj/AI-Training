class Sensor:
    def read(self): pass


class TempSensor(Sensor):
    def read(self): return "Temperature: 30C"


class PressureSensor(Sensor):
    def read(self): return "Pressure: 2 bar"


s = TempSensor()
print(s.read())
