# Week 15 - Final Project Guidelines

## Project: Library Management System

Build a comprehensive Library Management System that demonstrates all OOP concepts learned throughout the course.

## Requirements

### Core Classes

#### 1. Book
- Attributes: ISBN, title, author, publisher, year, copies_available, category
- Methods: borrow(), return_book(), is_available()

#### 2. Member
- Attributes: member_id, name, email, phone, borrowed_books, membership_type
- Methods: borrow_book(), return_book(), get_borrowed_books()

#### 3. Library
- Attributes: name, books, members, transactions
- Methods: add_book(), remove_book(), register_member(), process_borrow(), process_return()

#### 4. Transaction
- Attributes: transaction_id, member, book, date_borrowed, date_due, date_returned, fine
- Methods: calculate_fine(), is_overdue()

### OOP Concepts to Demonstrate

#### Inheritance
- Create `Book` hierarchy: `FictionBook`, `NonFictionBook`, `ReferenceBook`
- Create `Member` hierarchy: `StudentMember`, `FacultyMember`, `PublicMember`
  - Different borrowing limits
  - Different borrowing periods

#### Encapsulation
- Private attributes with getters/setters
- Validate all inputs
- Protect sensitive data

#### Polymorphism
- `calculate_fee()` method behaves differently for different member types
- `get_description()` method for different book types

#### Abstraction
- Abstract `LibraryItem` class
- Abstract `User` class
- Interfaces for `Borrowable`, `Searchable`

#### Exception Handling
- `BookNotFoundException`
- `MemberNotFoundException`
- `BookUnavailableException`
- `MaxBorrowLimitException`

#### Design Patterns
- **Singleton**: Library instance
- **Factory**: Create different types of books/members
- **Observer**: Notify members about due dates
- **Strategy**: Different fine calculation strategies

### Features to Implement

#### Basic Features
1. Add/Remove/Update books
2. Register/Update members
3. Borrow/Return books
4. Search books (by title, author, ISBN, category)
5. View member history
6. Calculate and collect fines

#### Advanced Features
1. Reservation system for unavailable books
2. Automatic overdue notifications
3. Generate reports (most borrowed books, active members, etc.)
4. Recommendation system based on borrowing history
5. Multi-user access with different privileges (Admin, Librarian, Member)

### File I/O Requirements
- Save/Load books from JSON/CSV
- Save/Load members from JSON/CSV
- Transaction history persistence
- Export reports

### Implementation Requirements

#### Python Version
- Use property decorators
- Implement context managers for file operations
- Use list comprehensions where appropriate
- Implement magic methods (`__str__`, `__repr__`, etc.)

#### C++ Version
- Use smart pointers for memory management
- Implement proper copy/move constructors
- Use STL containers (vector, map, set)
- Implement operator overloading where appropriate

## Deliverables

### 1. Source Code
- Well-organized directory structure
- Separate files for each class
- Main program file
- Both Python and C++ implementations

### 2. Documentation
- README with setup instructions
- Class diagrams (UML)
- API documentation
- Usage examples

### 3. Testing
- Test cases for each class
- Integration tests
- Sample data files

### 4. Report
- Design decisions
- OOP concepts application
- Challenges faced
- Future enhancements

## Directory Structure

```
final-project/
├── python/
│   ├── models/
│   │   ├── book.py
│   │   ├── member.py
│   │   ├── library.py
│   │   └── transaction.py
│   ├── exceptions/
│   │   └── exceptions.py
│   ├── utils/
│   │   └── file_handler.py
│   ├── main.py
│   └── tests/
│       └── test_library.py
├── cpp/
│   ├── include/
│   │   ├── Book.h
│   │   ├── Member.h
│   │   ├── Library.h
│   │   └── Transaction.h
│   ├── src/
│   │   ├── Book.cpp
│   │   ├── Member.cpp
│   │   ├── Library.cpp
│   │   └── Transaction.cpp
│   ├── main.cpp
│   └── Makefile
├── data/
│   ├── books.json
│   └── members.json
├── docs/
│   ├── UML_diagrams/
│   └── API_documentation.md
└── README.md
```

## Evaluation Rubric (100 points)

### Code Quality (30 points)
- Code organization and structure (10)
- Naming conventions and readability (10)
- Comments and documentation (10)

### OOP Implementation (40 points)
- Proper use of inheritance (10)
- Encapsulation and data hiding (10)
- Polymorphism implementation (10)
- Design patterns usage (10)

### Functionality (20 points)
- All required features working (15)
- Error handling (5)

### Documentation (10 points)
- README and setup guide (5)
- UML diagrams and design docs (5)

## Sample Code Skeleton

### Python Example

```python
# book.py
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Book(LibraryItem):
    def __init__(self, isbn, title, author):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__copies_available = 0
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def title(self):
        return self.__title
    
    # Add more methods...
```

### C++ Example

```cpp
// Book.h
#ifndef BOOK_H
#define BOOK_H

#include <string>

class LibraryItem {
public:
    virtual std::string getDescription() = 0;
    virtual ~LibraryItem() {}
};

class Book : public LibraryItem {
private:
    std::string isbn;
    std::string title;
    std::string author;
    int copiesAvailable;

public:
    Book(std::string isbn, std::string title, std::string author);
    std::string getISBN() const;
    std::string getTitle() const;
    // Add more methods...
};

#endif
```

## Tips for Success

1. **Start Early**: Break the project into smaller tasks
2. **Test Incrementally**: Test each component as you build
3. **Use Version Control**: Commit frequently with meaningful messages
4. **Follow SOLID Principles**: Keep classes focused and maintainable
5. **Document as You Go**: Don't leave documentation for the end
6. **Handle Errors Gracefully**: Think about edge cases
7. **Make It User-Friendly**: Good user interface/experience matters

## Bonus Points (10 extra points)

- Implement a GUI (using tkinter for Python or Qt for C++)
- Add user authentication system
- Implement advanced search with filters
- Create a web API version
- Add unit tests with good coverage

Good luck with your final project!
