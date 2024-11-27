class Car:
    # Attributes (properties)
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    # Method (behavior)
    def start(self):
        return f"The {self.color} {self.make} {self.model} starts."

    def stop(self):
        return f"The {self.color} {self.make} {self.model} stops."

