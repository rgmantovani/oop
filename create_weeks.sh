#!/bin/bash

# Week 3
cat > week-03/README.md << 'WEEK3'
# Week 3: Constructors and Destructors

## Learning Objectives
- Master different types of constructors
- Understand constructor overloading
- Learn about copy constructors
- Understand destructors and resource management
- Learn about RAII (Resource Acquisition Is Initialization) in C++

## Topics Covered
1. Default Constructors
2. Parameterized Constructors
3. Copy Constructors
4. Constructor Overloading
5. Destructors
6. Constructor Delegation (Python) and Initialization Lists (C++)

## Key Concepts

### Constructor Types
- **Default Constructor**: No parameters
- **Parameterized Constructor**: Takes arguments
- **Copy Constructor**: Creates copy from existing object

### Destructors
- Clean up resources when object is destroyed
- Python: `__del__()` (rarely needed)
- C++: `~ClassName()` (important for memory management)

## Practical Examples
See `python/` and `cpp/` directories for code examples.
WEEK3

# Week 4
cat > week-04/README.md << 'WEEK4'
# Week 4: Encapsulation and Access Modifiers

## Learning Objectives
- Understand the principle of encapsulation
- Learn about access modifiers (public, private, protected)
- Master getter and setter methods
- Understand property decorators in Python
- Learn about access control in C++

## Topics Covered
1. Encapsulation Principle
2. Access Modifiers: Public, Private, Protected
3. Getter and Setter Methods
4. Property Decorators (@property in Python)
5. Data Hiding and Information Hiding
6. Benefits of Encapsulation

## Key Concepts

### Access Control
**Python:**
- Public: `variable`
- Protected: `_variable` (convention)
- Private: `__variable` (name mangling)

**C++:**
- `public:` accessible from anywhere
- `private:` accessible only within class
- `protected:` accessible in class and derived classes

## Practical Examples
See `python/` and `cpp/` directories for implementations.
WEEK4

# Week 5
cat > week-05/README.md << 'WEEK5'
# Week 5: Inheritance - Part 1 (Single Inheritance)

## Learning Objectives
- Understand the concept of inheritance
- Learn single inheritance syntax
- Understand parent-child (base-derived) class relationships
- Learn method overriding
- Understand the `super()` function in Python
- Learn about base class initialization in C++

## Topics Covered
1. Introduction to Inheritance
2. Single Inheritance
3. IS-A Relationship
4. Method Overriding
5. Accessing Parent Class Members
6. Constructor Chaining

## Key Concepts

### Inheritance Syntax
**Python:**
```python
class Child(Parent):
    def __init__(self):
        super().__init__()
```

**C++:**
```cpp
class Child : public Parent {
public:
    Child() : Parent() {}
};
```

## Practical Examples
See implementation examples in `python/` and `cpp/` directories.
WEEK5

echo "Created weeks 3-5"
