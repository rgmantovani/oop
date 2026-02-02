"""
Week 8 - Abstract Classes in Python
"""

from abc import ABC, abstractmethod
import math

# Example 1: Shape hierarchy with abstract base class
class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass
    
    def description(self):
        """Concrete method available to all subclasses"""
        return f"This is a {self.__class__.__name__}"


class Rectangle(Shape):
    """Concrete implementation of Shape"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Concrete implementation of Shape"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


# Example 2: Payment system with interface-like abstract class
class PaymentMethod(ABC):
    """Abstract class defining payment interface"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Process a payment"""
        pass
    
    @abstractmethod
    def refund(self, amount):
        """Process a refund"""
        pass


class CreditCard(PaymentMethod):
    """Credit card payment implementation"""
    
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        print(f"Processing ${amount} payment with Credit Card ending in {self.card_number[-4:]}")
        return True
    
    def refund(self, amount):
        print(f"Refunding ${amount} to Credit Card ending in {self.card_number[-4:]}")
        return True


class PayPal(PaymentMethod):
    """PayPal payment implementation"""
    
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        print(f"Processing ${amount} payment via PayPal account {self.email}")
        return True
    
    def refund(self, amount):
        print(f"Refunding ${amount} to PayPal account {self.email}")
        return True


if __name__ == "__main__":
    print("=" * 60)
    print("Abstract Classes - Shape Hierarchy")
    print("=" * 60)
    
    # Cannot instantiate abstract class
    # shape = Shape()  # This would raise TypeError
    
    rect = Rectangle(5, 10)
    print(f"{rect.description()}")
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    
    print()
    
    circle = Circle(7)
    print(f"{circle.description()}")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")
    
    print("\n" + "=" * 60)
    print("Abstract Classes - Payment System")
    print("=" * 60)
    
    payment1 = CreditCard("1234567890123456")
    payment1.process_payment(100.50)
    payment1.refund(25.00)
    
    print()
    
    payment2 = PayPal("user@example.com")
    payment2.process_payment(75.25)
    payment2.refund(10.00)
