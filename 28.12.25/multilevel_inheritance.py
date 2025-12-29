# Multi-Level Inheritance in Python

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Mammal(Animal):
    def __init__(self, name, warm_blooded=True):
        super().__init__(name)
        self.warm_blooded = warm_blooded
    
    def breathe(self):
        print(f"{self.name} breathes air")

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} barks: Woof! Woof!")

# Main
if __name__ == "__main__":
    dog = Dog("Max", "Labrador")
    dog.eat()
    dog.breathe()
    dog.bark()
