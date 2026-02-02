"""
Week 1 - Exercise Solutions (Python)
"""

from datetime import datetime

# Exercise 1: Car Class
class Car:
    """A class to represent a car"""
    
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def display_info(self):
        """Display car information"""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
    
    def age(self):
        """Calculate car age"""
        current_year = datetime.now().year
        return current_year - self.year


# Exercise 2: Rectangle Class
class Rectangle:
    """A class to represent a rectangle"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Check if it's a square"""
        return self.width == self.height


# Exercise 3: BankAccount Class
class BankAccount:
    """A class to represent a bank account"""
    
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > self.balance:
            print(f"Insufficient funds! Current balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
    
    def display_balance(self):
        """Display current balance"""
        print(f"Account {self.account_number} - {self.owner_name}")
        print(f"Current Balance: ${self.balance:.2f}")


# Test the implementations
if __name__ == "__main__":
    print("=" * 60)
    print("Exercise 1: Car Class")
    print("=" * 60)
    
    car1 = Car("Toyota", "Camry", 2020, "Silver")
    car2 = Car("Honda", "Civic", 2018, "Blue")
    car3 = Car("Ford", "Mustang", 2022, "Red")
    
    car1.display_info()
    print(f"Age: {car1.age()} years\n")
    
    car2.display_info()
    print(f"Age: {car2.age()} years\n")
    
    car3.display_info()
    print(f"Age: {car3.age()} years\n")
    
    print("=" * 60)
    print("Exercise 2: Rectangle Class")
    print("=" * 60)
    
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(7, 7)
    rect3 = Rectangle(3.5, 8.2)
    
    print(f"Rectangle 1: {rect1.width} x {rect1.height}")
    print(f"Area: {rect1.area()}, Perimeter: {rect1.perimeter()}")
    print(f"Is square? {rect1.is_square()}\n")
    
    print(f"Rectangle 2: {rect2.width} x {rect2.height}")
    print(f"Area: {rect2.area()}, Perimeter: {rect2.perimeter()}")
    print(f"Is square? {rect2.is_square()}\n")
    
    print(f"Rectangle 3: {rect3.width} x {rect3.height}")
    print(f"Area: {rect3.area():.2f}, Perimeter: {rect3.perimeter():.2f}")
    print(f"Is square? {rect3.is_square()}\n")
    
    print("=" * 60)
    print("Exercise 3: BankAccount Class")
    print("=" * 60)
    
    account = BankAccount("ACC001", "John Doe", 1000.0)
    account.display_balance()
    print()
    
    account.deposit(500.0)
    account.withdraw(200.0)
    account.withdraw(2000.0)  # Should fail
    print()
    account.display_balance()
