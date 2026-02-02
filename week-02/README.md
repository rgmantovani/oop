# Week 2: Classes and Objects - Deep Dive

## Learning Objectives
- Understand the anatomy of a class
- Learn about instance variables and class variables
- Master constructors and initialization
- Understand the concept of `self` (Python) and `this` (C++)
- Learn about object lifecycle

## Topics Covered
1. Class Members: Attributes and Methods
2. Instance vs Class Variables
3. Constructors and Initialization
4. The `self` keyword in Python
5. The `this` pointer in C++
6. Object Creation and Destruction

## Theory

### Instance Variables vs Class Variables

**Instance Variables**: Unique to each object instance
- In Python: defined in `__init__` with `self.`
- In C++: defined as private/public members

**Class Variables**: Shared among all instances of a class
- In Python: defined at class level
- In C++: defined as `static` members

### Constructors
Special methods called when an object is created:
- **Python**: `__init__(self, ...)`
- **C++**: Method with same name as class

### Destructors
Called when an object is destroyed:
- **Python**: `__del__(self)` (rarely used, garbage collected)
- **C++**: `~ClassName()` (important for resource cleanup)

## Practical Examples

See the `python/` and `cpp/` directories for code examples.

## Exercises

Check the `exercises/` directory for practice problems.
