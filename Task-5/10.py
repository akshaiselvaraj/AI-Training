class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def turn_on(self): pass
    def turn_off(self): pass

class Light(Device):
    def turn_on(self): print("Light ON")
    def turn_off(self): print("Light OFF")

class Fan(Device):
    def turn_on(self): print("Fan ON")
    def turn_off(self): print("Fan OFF")

d = Light(1)
d.turn_on()
