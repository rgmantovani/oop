"""
Week 2 - Constructors and Destructors in Python
"""

class Resource:
    """Demonstrates constructor and destructor"""
    
    resource_count = 0
    
    def __init__(self, name, size):
        """Constructor - called when object is created"""
        self.name = name
        self.size = size
        Resource.resource_count += 1
        print(f"Resource '{self.name}' created (size: {self.size} MB)")
        print(f"Total resources: {Resource.resource_count}")
    
    def __del__(self):
        """Destructor - called when object is destroyed"""
        Resource.resource_count -= 1
        print(f"Resource '{self.name}' destroyed")
        print(f"Remaining resources: {Resource.resource_count}")


class Point:
    """A class representing a 2D point"""
    
    def __init__(self, x=0, y=0):
        """Constructor with default parameters"""
        self.x = x
        self.y = y
        print(f"Point created at ({self.x}, {self.y})")
    
    def distance_from_origin(self):
        """Calculate distance from origin"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        """String representation"""
        return f"Point({self.x}, {self.y})"


class BankAccount:
    """Bank account with multiple constructor options"""
    
    def __init__(self, account_number, owner_name, balance=0.0, account_type="Savings"):
        """
        Constructor with default parameters
        
        Args:
            account_number: Account identifier
            owner_name: Name of account owner
            balance: Initial balance (default 0.0)
            account_type: Type of account (default "Savings")
        """
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.account_type = account_type
        print(f"Account created: {account_number} - {owner_name}")
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"BankAccount('{self.account_number}', '{self.owner_name}', {self.balance}, '{self.account_type}')"


if __name__ == "__main__":
    print("=" * 60)
    print("Resource Management Example")
    print("=" * 60)
    
    res1 = Resource("Image1", 5)
    res2 = Resource("Video1", 100)
    print()
    
    # Delete an object explicitly
    del res1
    print()
    
    res3 = Resource("Audio1", 3)
    print("\nEnd of program - remaining objects will be destroyed\n")
    
    print("=" * 60)
    print("Point Example")
    print("=" * 60)
    
    p1 = Point()  # Default constructor
    p2 = Point(3, 4)  # Custom coordinates
    
    print(f"p1: {p1}, Distance: {p1.distance_from_origin():.2f}")
    print(f"p2: {p2}, Distance: {p2.distance_from_origin():.2f}")
    
    print("\n" + "=" * 60)
    print("BankAccount Example")
    print("=" * 60)
    
    # Different ways to create objects
    acc1 = BankAccount("ACC001", "John Doe")
    acc2 = BankAccount("ACC002", "Jane Smith", 1000.0)
    acc3 = BankAccount("ACC003", "Bob Johnson", 5000.0, "Checking")
    
    print(f"\n{repr(acc1)}")
    print(f"{repr(acc2)}")
    print(f"{repr(acc3)}")
