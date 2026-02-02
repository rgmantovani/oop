"""
Week 1 - Comparing Procedural and OOP approaches
"""

# PROCEDURAL APPROACH
print("=" * 50)
print("PROCEDURAL APPROACH")
print("=" * 50)

# Data stored in separate variables
book1_title = "Python Programming"
book1_author = "John Doe"
book1_pages = 350

book2_title = "C++ Fundamentals"
book2_author = "Jane Smith"
book2_pages = 420

# Functions to operate on data
def display_book(title, author, pages):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Pages: {pages}")

display_book(book1_title, book1_author, book1_pages)
print()
display_book(book2_title, book2_author, book2_pages)

print("\n" + "=" * 50)
print("OBJECT-ORIENTED APPROACH")
print("=" * 50)

# OOP APPROACH
class Book:
    """A class to represent a book"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        """Display book information"""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
    
    def is_long_book(self):
        """Check if book is considered long"""
        return self.pages > 400

# Creating objects
book1 = Book("Python Programming", "John Doe", 350)
book2 = Book("C++ Fundamentals", "Jane Smith", 420)

# Using objects
book1.display_info()
print(f"Is long book? {book1.is_long_book()}")
print()

book2.display_info()
print(f"Is long book? {book2.is_long_book()}")

print("\n" + "=" * 50)
print("ADVANTAGES OF OOP:")
print("- Data and methods bundled together")
print("- Better organization and reusability")
print("- Easier to maintain and extend")
print("- Models real-world entities naturally")
