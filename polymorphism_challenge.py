# Base class for Animals
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")


# Dog subclass
class Dog(Animal):
    def move(self):
        return "Running 🐕"


# Fish subclass
class Fish(Animal):
    def move(self):
        return "Swimming 🐟"


# Base class for Vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")


# Car subclass
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


# Plane subclass
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


# Demonstrating polymorphism
animals = [Dog(), Fish()]
vehicles = [Car(), Plane()]

for animal in animals:
    print(animal.move())  # Prints "Running 🐕" and "Swimming 🐟"

for vehicle in vehicles:
    print(vehicle.move())  # Prints "Driving 🚗" and "Flying ✈️"
