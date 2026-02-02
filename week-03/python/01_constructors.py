"""
Week 3 - Constructor Types in Python
"""

import math

class Point:
    """2D Point with multiple initialization options"""
    
    def __init__(self, x=0, y=0):
        """Default and parameterized constructor combined"""
        self.x = x
        self.y = y
    
    @classmethod
    def from_tuple(cls, point_tuple):
        """Alternative constructor from tuple"""
        return cls(point_tuple[0], point_tuple[1])
    
    @classmethod
    def from_polar(cls, r, theta):
        """Alternative constructor from polar coordinates"""
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return cls(x, y)
    
    def copy(self):
        """Copy method (Python doesn't have copy constructor like C++)"""
        return Point(self.x, self.y)
    
    def distance_to(self, other):
        """Calculate distance to another point"""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)
    
    def __str__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"


class Person:
    """Person class with comprehensive constructor"""
    
    def __init__(self, name, age=0, email=None, phone=None):
        """
        Constructor with default parameters
        
        Args:
            name: Person's name (required)
            age: Person's age (default 0)
            email: Email address (optional)
            phone: Phone number (optional)
        """
        self.name = name
        self.age = age
        self.email = email if email else "Not provided"
        self.phone = phone if phone else "Not provided"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age}, '{self.email}', '{self.phone}')"


if __name__ == "__main__":
    print("=" * 60)
    print("Point Class - Multiple Construction Methods")
    print("=" * 60)
    
    # Default constructor
    p1 = Point()
    print(f"Default: {p1}")
    
    # Parameterized constructor
    p2 = Point(3, 4)
    print(f"Parameterized: {p2}")
    
    # From tuple
    p3 = Point.from_tuple((5, 12))
    print(f"From tuple: {p3}")
    
    # From polar coordinates
    p4 = Point.from_polar(5, math.pi/4)
    print(f"From polar: {p4}")
    
    # Copy
    p5 = p2.copy()
    print(f"Copy of p2: {p5}")
    
    print(f"\nDistance from p2 to p3: {p2.distance_to(p3):.2f}")
    
    print("\n" + "=" * 60)
    print("Person Class - Constructor with Defaults")
    print("=" * 60)
    
    person1 = Person("Alice")
    person2 = Person("Bob", 25)
    person3 = Person("Charlie", 30, "charlie@email.com")
    person4 = Person("Diana", 28, "diana@email.com", "555-1234")
    
    print(repr(person1))
    print(repr(person2))
    print(repr(person3))
    print(repr(person4))
