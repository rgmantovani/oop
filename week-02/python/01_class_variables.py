"""
Week 2 - Instance vs Class Variables in Python
"""

class Counter:
    """Demonstrates instance and class variables"""
    
    # Class variable - shared by all instances
    total_count = 0
    
    def __init__(self, name):
        """Constructor"""
        # Instance variable - unique to each instance
        self.name = name
        self.count = 0
        Counter.total_count += 1
    
    def increment(self):
        """Increment both instance and class counters"""
        self.count += 1
        Counter.total_count += 1
    
    def display(self):
        """Display counter information"""
        print(f"{self.name}: count = {self.count}")
        print(f"Total count (class level): {Counter.total_count}")


class Employee:
    """Employee class with class and instance variables"""
    
    # Class variables
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary):
        """Initialize employee"""
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable
        self.emp_id = Employee.employee_count + 1  # Instance variable
        Employee.employee_count += 1  # Increment class variable
    
    def display_info(self):
        """Display employee information"""
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Company: {Employee.company_name}")
    
    @classmethod
    def get_employee_count(cls):
        """Class method to get total employee count"""
        return cls.employee_count
    
    @classmethod
    def change_company_name(cls, new_name):
        """Class method to change company name"""
        cls.company_name = new_name


if __name__ == "__main__":
    print("=" * 60)
    print("Counter Example")
    print("=" * 60)
    
    counter1 = Counter("Counter A")
    counter2 = Counter("Counter B")
    
    print(f"Initial total count: {Counter.total_count}")
    
    counter1.increment()
    counter1.increment()
    counter1.display()
    print()
    
    counter2.increment()
    counter2.display()
    print()
    
    print("=" * 60)
    print("Employee Example")
    print("=" * 60)
    
    emp1 = Employee("Alice", 75000)
    emp2 = Employee("Bob", 65000)
    emp3 = Employee("Charlie", 80000)
    
    emp1.display_info()
    print()
    emp2.display_info()
    print()
    
    print(f"Total employees: {Employee.get_employee_count()}")
    
    # Change company name (affects all employees)
    Employee.change_company_name("New Tech Corp")
    print(f"\nAfter company name change:")
    emp3.display_info()
