"""
Week 6 - Multiple Inheritance in Python
"""

# Example 1: Simple Multiple Inheritance
class Flyable:
    """Mixin for flying capability"""
    
    def fly(self):
        print(f"{self.__class__.__name__} is flying")


class Swimmable:
    """Mixin for swimming capability"""
    
    def swim(self):
        print(f"{self.__class__.__name__} is swimming")


class Animal:
    """Base animal class"""
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")


class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from Animal, Flyable, and Swimmable"""
    
    def __init__(self, name):
        super().__init__(name)
    
    def quack(self):
        print(f"{self.name} says: Quack!")


# Example 2: Diamond Problem and MRO
class A:
    def process(self):
        print("Process in A")


class B(A):
    def process(self):
        print("Process in B")
        super().process()


class C(A):
    def process(self):
        print("Process in C")
        super().process()


class D(B, C):
    """Diamond inheritance: D -> B -> A and D -> C -> A"""
    
    def process(self):
        print("Process in D")
        super().process()


if __name__ == "__main__":
    print("=" * 60)
    print("Multiple Inheritance - Duck Example")
    print("=" * 60)
    
    duck = Duck("Donald")
    duck.eat()  # From Animal
    duck.fly()  # From Flyable
    duck.swim()  # From Swimmable
    duck.quack()  # From Duck
    
    print("\n" + "=" * 60)
    print("Diamond Problem and MRO")
    print("=" * 60)
    
    d = D()
    d.process()
    
    print("\nMethod Resolution Order for class D:")
    print(D.__mro__)
    
    print("\nMRO in readable format:")
    for i, cls in enumerate(D.__mro__):
        print(f"{i}: {cls.__name__}")
