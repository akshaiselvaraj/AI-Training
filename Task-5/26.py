class Storage:
    def limit(self): pass

class Free(Storage):
    def limit(self): return "5GB"

class Pro(Storage):
    def limit(self): return "100GB"

s = Pro()
print("Storage:", s.limit())
