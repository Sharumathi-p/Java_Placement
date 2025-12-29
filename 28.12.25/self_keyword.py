# Self Keyword in Python (equivalent to 'this' in Java)

class Person:
    def __init__(self, name, age):
        self.name = name  # self refers to the instance
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old")
    
    def compare_age(self, other):
        if self.age > other.age:
            print(f"{self.name} is older than {other.name}")
        elif self.age < other.age:
            print(f"{self.name} is younger than {other.name}")
        else:
            print(f"{self.name} and {other.name} are the same age")

# Main
if __name__ == "__main__":
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    
    person1.display()
    person2.display()
    person1.compare_age(person2)
