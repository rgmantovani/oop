#!/bin/bash

# Week 6 README
cat > week-06/README.md << 'EOF'
# Week 6: Inheritance - Part 2 (Multiple Inheritance)

## Learning Objectives
- Understand multiple inheritance
- Learn about the diamond problem
- Master Method Resolution Order (MRO) in Python
- Understand virtual inheritance in C++
- Learn when to use multiple inheritance

## Topics Covered
1. Multiple Inheritance Syntax
2. Diamond Problem and Solutions
3. Method Resolution Order (Python)
4. Virtual Inheritance (C++)
5. Mix-in Classes
6. Best Practices for Multiple Inheritance

## Key Concepts
Multiple inheritance allows a class to inherit from more than one base class.
Python handles this with MRO, C++ uses virtual inheritance for diamond problem.
EOF

# Week 7 README
cat > week-07/README.md << 'EOF'
# Week 7: Polymorphism - Part 1 (Method Overloading & Overriding)

## Learning Objectives
- Understand polymorphism concept
- Learn method overloading techniques
- Master method overriding
- Understand dynamic binding
- Learn about virtual functions in C++

## Topics Covered
1. Polymorphism Concept
2. Method Overloading (Compile-time Polymorphism)
3. Method Overriding (Runtime Polymorphism)
4. Virtual Functions in C++
5. Dynamic Method Dispatch
6. The `super()` function

## Key Concepts
Polymorphism means "many forms" - same interface, different implementations.
EOF

# Week 8 README
cat > week-08/README.md << 'EOF'
# Week 8: Polymorphism - Part 2 (Abstract Classes & Interfaces)

## Learning Objectives
- Understand abstract classes
- Learn about abstract methods
- Master interfaces in OOP
- Understand the ABC module in Python
- Learn pure virtual functions in C++

## Topics Covered
1. Abstract Classes
2. Abstract Methods
3. Interfaces and Protocols
4. ABC Module (Python)
5. Pure Virtual Functions (C++)
6. Abstract Base Classes

## Key Concepts
Abstract classes cannot be instantiated and serve as templates for derived classes.
EOF

# Week 9 README
cat > week-09/README.md << 'EOF'
# Week 9: Operator Overloading and Special Methods

## Learning Objectives
- Understand operator overloading
- Learn special methods in Python (dunder methods)
- Master operator overloading in C++
- Understand comparison operators
- Learn arithmetic operator overloading

## Topics Covered
1. Operator Overloading Concept
2. Python Magic Methods (__add__, __str__, etc.)
3. C++ Operator Overloading
4. Comparison Operators
5. Arithmetic Operators
6. Friend Functions in C++

## Key Concepts
Operator overloading allows custom behavior for built-in operators.
EOF

# Week 10 README
cat > week-10/README.md << 'EOF'
# Week 10: Exception Handling in OOP

## Learning Objectives
- Understand exception handling in OOP context
- Learn try-catch-finally blocks
- Master custom exceptions
- Understand exception hierarchies
- Learn RAII and exception safety in C++

## Topics Covered
1. Exception Handling Basics
2. Try-Catch-Finally Blocks
3. Custom Exception Classes
4. Exception Hierarchies
5. Exception Safety
6. RAII Pattern in C++

## Key Concepts
Exception handling provides a way to handle runtime errors gracefully.
EOF

# Week 11 README
cat > week-11/README.md << 'EOF'
# Week 11: File I/O and Serialization

## Learning Objectives
- Master file operations in OOP
- Learn object serialization
- Understand pickle (Python) and serialization (C++)
- Learn about JSON and XML handling
- Understand persistent storage

## Topics Covered
1. File I/O Operations
2. Object Serialization
3. Pickle Module (Python)
4. JSON Serialization
5. Binary vs Text Files
6. Stream Operations in C++

## Key Concepts
Serialization converts objects to a format that can be stored and reconstructed.
EOF

# Week 12 README
cat > week-12/README.md << 'EOF'
# Week 12: Design Patterns - Part 1 (Creational Patterns)

## Learning Objectives
- Understand design patterns importance
- Learn Singleton pattern
- Master Factory pattern
- Understand Builder pattern
- Learn Prototype pattern

## Topics Covered
1. Introduction to Design Patterns
2. Singleton Pattern
3. Factory Method Pattern
4. Abstract Factory Pattern
5. Builder Pattern
6. Prototype Pattern

## Key Concepts
Creational patterns deal with object creation mechanisms.
EOF

# Week 13 README
cat > week-13/README.md << 'EOF'
# Week 13: Design Patterns - Part 2 (Structural Patterns)

## Learning Objectives
- Understand structural patterns
- Learn Adapter pattern
- Master Decorator pattern
- Understand Facade pattern
- Learn Proxy pattern

## Topics Covered
1. Adapter Pattern
2. Bridge Pattern
3. Composite Pattern
4. Decorator Pattern
5. Facade Pattern
6. Proxy Pattern

## Key Concepts
Structural patterns deal with object composition and relationships.
EOF

# Week 14 README
cat > week-14/README.md << 'EOF'
# Week 14: Design Patterns - Part 3 (Behavioral Patterns)

## Learning Objectives
- Understand behavioral patterns
- Learn Observer pattern
- Master Strategy pattern
- Understand Template Method
- Learn Command pattern

## Topics Covered
1. Observer Pattern
2. Strategy Pattern
3. Template Method Pattern
4. Command Pattern
5. Iterator Pattern
6. State Pattern

## Key Concepts
Behavioral patterns deal with object interaction and responsibility distribution.
EOF

# Week 15 README
cat > week-15/README.md << 'EOF'
# Week 15: Final Project - Complete OOP Application

## Project Requirements
Build a complete application demonstrating all OOP concepts learned.

## Suggested Projects

### 1. Library Management System
- Books, Members, Transactions
- Inheritance (different book types)
- Encapsulation (private data)
- Polymorphism (different member types)
- File I/O for persistence

### 2. Banking System
- Accounts (Savings, Checking, Credit)
- Customers and Transactions
- Exception handling
- Design patterns implementation

### 3. Student Management System
- Students, Courses, Grades
- Teachers and Administrators
- Multiple inheritance concepts
- Comprehensive OOP features

## Deliverables
1. Complete source code (Python and C++)
2. Documentation
3. UML diagrams
4. Test cases
5. User manual

## Evaluation Criteria
- Code organization
- OOP principles application
- Documentation quality
- Functionality completeness
- Error handling
EOF

echo "All week READMEs created successfully"
