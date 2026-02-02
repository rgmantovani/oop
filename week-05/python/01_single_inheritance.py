"""
Week 5 - Single Inheritance in Python
"""

# Base class
class Animal:
    """Base class representing an animal"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        """Method that can be inherited"""
        print(f"{self.name} is eating")
    
    def sleep(self):
        """Method that can be inherited"""
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        """Method to be overridden in child classes"""
        print(f"{self.name} makes a sound")


# Derived class
class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):
        """Override parent method"""
        print(f"{self.name} barks: Woof! Woof!")
    
    def fetch(self):
        """New method specific to Dog"""
        print(f"{self.name} is fetching the ball")


class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        """Override parent method"""
        print(f"{self.name} meows: Meow!")
    
    def climb(self):
        """New method specific to Cat"""
        print(f"{self.name} is climbing a tree")


class Vehicle:
    """Base class for vehicles"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.brand} {self.model} is starting")
    
    def stop(self):
        print(f"{self.brand} {self.model} is stopping")


class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def honk(self):
        print("Beep beep!")


if __name__ == "__main__":
    print("=" * 60)
    print("Animal Hierarchy")
    print("=" * 60)
    
    # Create Dog object
    dog = Dog("Buddy", 3, "Golden Retriever")
    print(f"Name: {dog.name}, Age: {dog.age}, Breed: {dog.breed}")
    dog.eat()  # Inherited method
    dog.sleep()  # Inherited method
    dog.make_sound()  # Overridden method
    dog.fetch()  # Dog-specific method
    
    print("\n" + "=" * 60)
    
    # Create Cat object
    cat = Cat("Whiskers", 2, "Orange")
    print(f"Name: {cat.name}, Age: {cat.age}, Color: {cat.color}")
    cat.eat()  # Inherited method
    cat.make_sound()  # Overridden method
    cat.climb()  # Cat-specific method
    
    print("\n" + "=" * 60)
    print("Vehicle Hierarchy")
    print("=" * 60)
    
    car = Car("Toyota", "Camry", 2022, 4)
    print(f"{car.brand} {car.model} ({car.year}) - {car.num_doors} doors")
    car.start()  # Inherited method
    car.honk()  # Car-specific method
    car.stop()  # Inherited method
