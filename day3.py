class Temp:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        return (self.temperature - 32) * 5.0 / 9.0

    def to_fahrenheit(self):
        return (self.temperature * 9.0 / 5.0) + 32
obj=Temp(100)
print(obj)