# Assignment 1: Design Your Own Class! 🏗️

class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name} has the power of {self.power}"
    
#Activity 2: Polymorphism Challenge! 🎭

# Base class for Vehicles
class Vehicle:
    def move(self):
        pass  

# Car subclass
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane subclass
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Animal base class
class Animal:
    def move(self):
        pass  

# Dog subclass
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Fish subclass
class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

# Creating instances of each class
my_car = Car()
my_plane = Plane()
my_dog = Dog()
my_fish = Fish()

# Calling the move method for each object
my_car.move()    # Output: Driving 🚗
my_plane.move()  # Output: Flying ✈️
my_dog.move()    # Output: Running 🐕
my_fish.move()   # Output: Swimming 🐟
