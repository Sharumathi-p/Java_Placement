# Single Inheritance in Python

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks")
    
    def display_info(self):
        print(f"Dog: {self.name}, Breed: {self.breed}")

# Main
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    dog.display_info()
    dog.speak()
