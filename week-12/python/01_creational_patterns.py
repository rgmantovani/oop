"""
Week 12 - Creational Design Patterns in Python
"""

# 1. Singleton Pattern
class Singleton:
    """Ensures a class has only one instance"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = 0
        return cls._instance
    
    def increment(self):
        self.value += 1


class DatabaseConnection(Singleton):
    """Example: Database connection as singleton"""
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.host = "localhost"
            self.port = 5432
            self.initialized = True
    
    def connect(self):
        return f"Connected to {self.host}:{self.port}"


# 2. Factory Pattern
class Animal:
    """Base animal class"""
    
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    """Factory to create animals"""
    
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# 3. Builder Pattern
class Pizza:
    """Product class"""
    
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
    
    def __str__(self):
        return f"{self.size} pizza with {self.crust} crust and toppings: {', '.join(self.toppings)}"


class PizzaBuilder:
    """Builder class"""
    
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def set_crust(self, crust):
        self.pizza.crust = crust
        return self
    
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def build(self):
        return self.pizza


if __name__ == "__main__":
    print("=" * 60)
    print("Singleton Pattern")
    print("=" * 60)
    
    s1 = Singleton()
    s2 = Singleton()
    
    print(f"s1 is s2: {s1 is s2}")  # True - same instance
    
    s1.increment()
    print(f"s1.value: {s1.value}")
    print(f"s2.value: {s2.value}")  # Same value
    
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"\ndb1 is db2: {db1 is db2}")
    print(db1.connect())
    
    print("\n" + "=" * 60)
    print("Factory Pattern")
    print("=" * 60)
    
    dog = AnimalFactory.create_animal("dog")
    cat = AnimalFactory.create_animal("cat")
    
    print(f"Dog says: {dog.speak()}")
    print(f"Cat says: {cat.speak()}")
    
    print("\n" + "=" * 60)
    print("Builder Pattern")
    print("=" * 60)
    
    pizza = (PizzaBuilder()
            .set_size("Large")
            .set_crust("Thin")
            .add_topping("Cheese")
            .add_topping("Pepperoni")
            .add_topping("Mushrooms")
            .build())
    
    print(pizza)
