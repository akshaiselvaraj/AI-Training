class Update:
    def apply(self): pass


class OTA(Update):
    def apply(self): print("OTA Update applied")


class Manual(Update):
    def apply(self): print("Manual update applied")


u = OTA()
u.apply()
