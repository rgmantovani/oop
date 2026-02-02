# Week 1: Introduction to Object-Oriented Programming

## Learning Objectives
- Understand the fundamental concepts of OOP
- Learn the differences between procedural and object-oriented programming
- Understand the four pillars of OOP: Encapsulation, Inheritance, Polymorphism, and Abstraction
- Learn about **Composition** (HAS-A relationship)
- Set up Python and C++ development environments
- Write your first simple class in both languages
- Create composed objects (Player with Class and Race)

## Topics Covered
1. What is Object-Oriented Programming?
2. Procedural vs Object-Oriented Programming
3. The Four Pillars of OOP
4. Introduction to Classes and Objects
5. **Composition: The HAS-A Relationship**
6. Setting up development environments

## Theory

### What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects rather than functions and logic. Objects are instances of classes that contain both data (attributes) and behavior (methods).

### The Four Pillars of OOP

1. **Encapsulation**: Bundling data and methods that operate on that data within a single unit (class), and controlling access to them.

2. **Inheritance**: Mechanism where a new class inherits properties and methods from an existing class (IS-A relationship).

3. **Polymorphism**: Ability of objects to take on multiple forms. The same method can behave differently for different objects.

4. **Abstraction**: Hiding complex implementation details and showing only the necessary features of an object.

### Composition: The HAS-A Relationship

**Composition** is a fundamental OOP concept where one class contains objects of other classes as attributes. This represents a "HAS-A" relationship.

**Example:**
- A `Player` HAS-A `CharacterClass` (Warrior, Mage, Thief)
- A `Player` HAS-A `Race` (Human, Elf, Orc)
- A `Car` HAS-AN `Engine`
- A `House` HAS-A `Door`

**Why use Composition?**
- Models real-world relationships naturally
- Promotes code reuse without inheritance
- More flexible than inheritance
- Easier to change implementations

**Composition vs Inheritance:**
- **Inheritance (IS-A)**: A Dog IS-A Animal
- **Composition (HAS-A)**: A Player HAS-A Class, A Player HAS-A Race

In our RPG game:
```python
class Player:
    def __init__(self, name, character_class, race):
        self.name = name
        self.character_class = character_class  # Composition!
        self.race = race  # Composition!
```

The Player doesn't inherit from Class or Race; it *contains* them.

## Practical Examples

See the `python/` and `cpp/` directories for code examples in each language:
- `01_first_class.py/cpp` - Basic Student class
- `02_procedural_vs_oop.py/cpp` - Comparing approaches
- `03_composition_class_race.py/cpp` - **NEW: Composition with Player, Class, and Race**

## Key Example: Composition

### Python
```python
class CharacterClass:
    def __init__(self, name, primary_stat):
        self.name = name
        self.primary_stat = primary_stat

class Race:
    def __init__(self, name, special_ability):
        self.name = name
        self.special_ability = special_ability

class Player:
    def __init__(self, name, char_class, race):
        self.name = name
        self.character_class = char_class  # HAS-A Class
        self.race = race  # HAS-A Race

# Create composed objects
warrior_class = CharacterClass("Warrior", "Strength")
human_race = Race("Human", "Adaptability")
player = Player("Thorin", warrior_class, human_race)
```

### C++
```cpp
class CharacterClass {
private:
    string name;
    string primaryStat;
public:
    CharacterClass(string n, string stat) 
        : name(n), primaryStat(stat) {}
};

class Player {
private:
    string name;
    CharacterClass characterClass;  // HAS-A Class
    Race race;  // HAS-A Race
public:
    Player(string n, CharacterClass c, Race r) 
        : name(n), characterClass(c), race(r) {}
};
```

## Exercises

Check the `exercises/` directory for hands-on practice problems including:
- Creating Player with Class and Race composition
- Item class with enhanced properties
- Backpack with Item objects

## Additional Resources
- [Python Official Documentation](https://docs.python.org/3/tutorial/classes.html)
- [C++ Classes and Objects](https://cplusplus.com/doc/tutorial/classes/)
- [Composition vs Inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance)
