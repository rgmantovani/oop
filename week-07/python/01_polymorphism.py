"""
Week 7 - Polymorphism and Method Overriding in Python
"""

# Example 1: Method Overriding
class Shape:
    """Base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """To be overridden by subclasses"""
        return 0
    
    def describe(self):
        return f"This is a {self.name}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Override parent method"""
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Override parent method"""
        import math
        return math.pi * self.radius ** 2


# Example 2: Polymorphism in action
class Employee:
    """Base employee class"""
    
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def calculate_salary(self):
        """To be overridden"""
        return 0
    
    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: ${self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


def process_employees(employees):
    """Polymorphic function - works with any Employee subclass"""
    total_payroll = 0
    for emp in employees:
        emp.display_info()
        total_payroll += emp.calculate_salary()
    return total_payroll


if __name__ == "__main__":
    print("=" * 60)
    print("Method Overriding - Shapes")
    print("=" * 60)
    
    shapes = [
        Rectangle(5, 10),
        Circle(7),
        Rectangle(3, 8)
    ]
    
    for shape in shapes:
        print(f"{shape.describe()}: Area = {shape.area():.2f}")
    
    print("\n" + "=" * 60)
    print("Polymorphism - Employee System")
    print("=" * 60)
    
    employees = [
        FullTimeEmployee("Alice", "E001", 5000),
        HourlyEmployee("Bob", "E002", 25, 160),
        FullTimeEmployee("Charlie", "E003", 6000),
        HourlyEmployee("Diana", "E004", 30, 120)
    ]
    
    total = process_employees(employees)
    print(f"\nTotal Payroll: ${total}")
