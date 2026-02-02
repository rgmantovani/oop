"""
Week 1 - Introduction to OOP in Python
First Class Example
"""

# A simple class representing a Student
class Student:
    """A class to represent a student"""
    
    def __init__(self, name, age, student_id):
        """
        Constructor to initialize student object
        
        Args:
            name (str): Student's name
            age (int): Student's age
            student_id (str): Student's ID
        """
        self.name = name
        self.age = age
        self.student_id = student_id
    
    def display_info(self):
        """Display student information"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
    
    def greet(self):
        """Student greets"""
        return f"Hello, my name is {self.name}!"


# Main program
if __name__ == "__main__":
    # Creating objects (instances) of the Student class
    student1 = Student("Alice Johnson", 20, "S001")
    student2 = Student("Bob Smith", 22, "S002")
    
    # Using object methods
    print("Student 1 Information:")
    student1.display_info()
    print(student1.greet())
    
    print("\nStudent 2 Information:")
    student2.display_info()
    print(student2.greet())
