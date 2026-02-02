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
