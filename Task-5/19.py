class Model:
    def predict(self, data):
        pass

class LinearModel(Model):
    def predict(self, data):
        return sum(data)

class TreeModel(Model):
    def predict(self, data):
        return max(data)

m = TreeModel()
print("Prediction:", m.predict([2, 5, 3]))
