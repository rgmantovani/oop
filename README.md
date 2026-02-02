# Object-Oriented Programming Course
## Complete 15-Week Undergraduate Course in Python and C++
## Building an RPG Game Incrementally

Welcome to the comprehensive Object-Oriented Programming (OOP) course! This repository contains a complete 15-week curriculum designed for undergraduate students, featuring theoretical content, practical examples, and hands-on exercises in both **Python** and **C++**.

## 🎮 Unique Approach: Incremental RPG Development

Unlike traditional courses with isolated exercises, this course uses an **incremental development** approach:
- Build a single RPG game system over 15 weeks
- Each week adds new features using newly learned OOP concepts
- See how real-world applications evolve and grow
- Apply concepts immediately to your ongoing project
- End with a complete, playable RPG game!

**📖 Read the [Incremental Development Guide](INCREMENTAL_GUIDE.md) for the complete development roadmap.**

## Course Structure

The course is organized into 15 weekly modules, each containing:
- 📚 **README.md**: Learning objectives, theory, and key concepts
- 🐍 **python/**: Python code examples and implementations
- ⚙️ **cpp/**: C++ code examples and implementations
- 📝 **exercises/**: RPG-themed exercises building on previous weeks
- ✅ **solutions/**: Reference solutions for exercises

## Weekly Breakdown

### 🏗️ Part 1: Foundation (Weeks 1-3)
Build the core entities of your RPG:
- **[Week 1: Introduction to OOP](week-01/)** - Create Player, Item, and Backpack classes
- **[Week 2: Classes and Objects](week-02/)** - Add player registry, experience system, weapon durability
- **[Week 3: Constructors and Destructors](week-03/)** - Implement quest system with lifecycle

**By Week 3:** You'll have playable characters with inventory and quests

---

### 🛡️ Part 2: Core Principles (Weeks 4-5)
Strengthen your game with proper OOP principles:
- **[Week 4: Encapsulation](week-04/)** - Protect player stats, validate inventory operations
- **[Week 5: Inheritance - Part 1](week-05/)** - Create character hierarchy (Player, Enemy, NPC) and item types

**By Week 5:** You'll have a robust character system with multiple entity types

---

### ⚔️ Part 3: Advanced Inheritance (Weeks 6-7)
Add complexity and combat:
- **[Week 6: Inheritance - Part 2](week-06/)** - Multiple abilities (flying, swimming, stealth), hybrid characters
- **[Week 7: Polymorphism - Part 1](week-07/)** - Polymorphic combat system, quest rewards

**By Week 7:** You'll have a working combat system with diverse character abilities

---

### 🔮 Part 4: Abstraction and Special Methods (Weeks 8-9)
Add magic and intuitive operations:
- **[Week 8: Polymorphism - Part 2](week-08/)** - Abstract spell system, item interfaces
- **[Week 9: Operator Overloading](week-09/)** - Natural syntax for positions, items, stats

**By Week 9:** You'll have spellcasting and intuitive game operations

---

### 💾 Part 5: Error Handling and I/O (Weeks 10-11)
Make it robust and persistent:
- **[Week 10: Exception Handling](week-10/)** - Custom exceptions, safe operations
- **[Week 11: File I/O and Serialization](week-11/)** - Save/load system, persistence

**By Week 11:** You'll have a crash-proof game with save/load functionality

---

### 🎨 Part 6: Design Patterns (Weeks 12-14)
Professional software architecture:
- **[Week 12: Creational Patterns](week-12/)** - Singleton, Factory, Builder, Prototype
- **[Week 13: Structural Patterns](week-13/)** - Decorator, Adapter, Facade, Composite, Proxy
- **[Week 14: Behavioral Patterns](week-14/)** - Strategy, Observer, Command, Template, State

**By Week 14:** You'll have professional-grade architecture

---

### 🏆 Part 7: Final Project (Week 15)
Complete and polish:
- **[Week 15: Final Project](week-15/)** - Integration, game content, polish, documentation

**By Week 15:** You'll have a complete, playable RPG game!

---

## 🎯 Learning Objectives

### What You'll Build Throughout the Course

**Week 1-3: Foundation**
```
Player: "Hero" | Level 1 | HP: 100
Inventory: [Iron Sword, Health Potion x3]
Quest: Defeat the Goblin [Active]
```

**Week 4-7: Core Systems**
```
=== COMBAT ===
Hero (Warrior) attacks Goblin with Iron Sword
  → Damage: 45 (30 base + 15 fire enchantment)
Goblin HP: 55/100

Hero levels up! → Level 2
Quest Complete: Defeat the Goblin
Rewards: +100 XP, +50 Gold
```

**Week 8-11: Advanced Features**
```
Hero casts Fireball on Dragon
  → Mana cost: 30 (60/90 remaining)
  → Damage: 75 fire damage

Game saved successfully!
Save file: hero_save_01.json
```

**Week 12-15: Complete Game**
```
=== EPIC QUEST RPG ===
> New Game
Choose your class:
1. Warrior  2. Mage  3. Archer
> _
```

## Prerequisites

### For Python
- Python 3.8 or higher
- Basic understanding of programming concepts
- A text editor or IDE (VS Code, PyCharm, etc.)

### For C++
- C++11 or higher compiler (g++, clang++, or MSVC)
- Basic understanding of programming concepts
- A text editor or IDE (VS Code, CLion, Visual Studio, etc.)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/rgmantovani/oop.git
cd oop
```

### 2. Start with Week 1
```bash
cd week-01
# Read README.md first
# Then study examples in python/ and cpp/
# Finally, complete exercises/
```

### 3. Running Examples

**Python:**
```bash
cd week-01/python/
python3 01_first_class.py
```

**C++:**
```bash
cd week-01/cpp/
g++ -std=c++11 01_first_class.cpp -o first_class
./first_class
```

## Incremental Development Workflow

### Each Week Follow These Steps:

1. **📖 Read Theory**: Study the week's README.md
2. **👀 Study Examples**: Review Python and C++ implementations
3. **💻 Do Exercises**: Complete RPG exercises, building on previous weeks
4. **✅ Test**: Ensure new code integrates with previous weeks
5. **💾 Commit**: Version control your progress
6. **🔄 Refactor**: Improve previous code with new knowledge

### Example Weekly Workflow:

```bash
# Week 4 Example
cd week-04

# 1. Read theory on encapsulation
cat README.md

# 2. Study examples
python3 python/01_encapsulation.py

# 3. Do exercises: Make player stats private
cd exercises/
# ... implement your code ...

# 4. Test with previous weeks' code
python3 test_integration.py

# 5. Commit your work
git add .
git commit -m "Week 4: Added encapsulation to player stats"
```

## The RPG Game You'll Build

### Core Features
- ✅ Character creation with multiple classes
- ✅ Inventory system with different item types
- ✅ Combat system with multiple enemy types
- ✅ Quest system with various quest types
- ✅ Experience and leveling
- ✅ Spell casting system
- ✅ Equipment and enchantments
- ✅ Save/load functionality
- ✅ Multiple game areas
- ✅ NPC interactions

### Technical Features
- ✅ All four OOP pillars demonstrated
- ✅ Multiple inheritance hierarchies
- ✅ Abstract classes and interfaces
- ✅ Operator overloading
- ✅ Exception handling
- ✅ File I/O and serialization
- ✅ 10+ design patterns implemented
- ✅ Both Python and C++ versions

## Key Differences: Python vs C++

| Aspect | Python | C++ |
|--------|--------|-----|
| **Type System** | Dynamic typing | Static typing |
| **Memory Management** | Automatic (Garbage Collection) | Manual (new/delete) or smart pointers |
| **Syntax** | Simpler, more readable | More verbose, explicit |
| **Inheritance** | Multiple inheritance with MRO | Multiple inheritance with virtual |
| **Access Control** | Convention-based (_private) | Keyword-based (private, protected) |
| **Performance** | Slower, interpreted | Faster, compiled |
| **Development Speed** | Faster prototyping | Requires more setup |

## The Four Pillars of OOP

### 1. 🔒 Encapsulation
Bundling data and methods together, controlling access.
- **Week 4**: Make player stats private, validate operations
- **Applied**: Protected health/mana, validated inventory

### 2. 🧬 Inheritance
Mechanism where classes inherit from other classes.
- **Week 5-6**: Character hierarchy, multiple inheritance
- **Applied**: Player, Enemy, NPC all inherit from Character

### 3. 🎭 Polymorphism
Same interface, different implementations.
- **Week 7-8**: Polymorphic combat, abstract spells
- **Applied**: Any character can fight any other character

### 4. 🎨 Abstraction
Hiding complexity, showing only essentials.
- **Week 8**: Abstract classes, interfaces
- **Applied**: Abstract Character class, cannot instantiate

## Design Patterns You'll Implement

### Creational (Week 12)
- **Singleton**: GameManager
- **Factory**: CharacterFactory
- **Builder**: WeaponBuilder
- **Prototype**: Item cloning

### Structural (Week 13)
- **Decorator**: Item enchantments
- **Adapter**: Legacy system integration
- **Facade**: Combat system
- **Composite**: Nested inventory
- **Proxy**: Lazy asset loading

### Behavioral (Week 14)
- **Strategy**: Enemy AI
- **Observer**: Event system
- **Command**: Undo/redo
- **Template Method**: Quest workflows
- **State**: Player states

## Additional Resources

### Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [C++ Reference](https://en.cppreference.com/)
- [Incremental Development Guide](INCREMENTAL_GUIDE.md)

### Recommended Books
- "Python Object-Oriented Programming" by Steven F. Lott
- "Effective C++" by Scott Meyers
- "Design Patterns" by Gang of Four
- "Game Programming Patterns" by Robert Nystrom

### Practice Platforms
- [LeetCode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/)
- [Exercism](https://exercism.org/)

## Assessment

### Continuous Assessment
- Weekly exercises (50%)
- Code quality and OOP principles (20%)
- Integration with previous weeks (10%)

### Final Project (Week 15)
- Complete RPG game (40%)
- Documentation (10%)
- Presentation (10%)

## Contributing

This is an educational repository. To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Troubleshooting

### Common Issues

**Issue**: Code from previous week doesn't work
**Solution**: Check the solutions/ directory, ensure proper integration

**Issue**: Confused about inheritance hierarchy
**Solution**: Draw UML diagrams, visualize relationships

**Issue**: Game getting too complex
**Solution**: Refactor regularly, split into modules

## Support

- 📧 Create issues in the repository
- 💬 Discussion forum for questions
- 👥 Study groups recommended
- 📅 Office hours with instructor

## License

This course material is provided for educational purposes.

## Acknowledgments

This course teaches industry-standard OOP practices through game development, making learning engaging and practical.

---

## 🚀 Ready to Start?

1. **Read**: [Incremental Development Guide](INCREMENTAL_GUIDE.md)
2. **Begin**: [Week 1 - Introduction to OOP](week-01/)
3. **Build**: Your own RPG game!

**By the end of this course, you'll have:**
- ✅ Mastery of OOP concepts
- ✅ A complete RPG game you built from scratch
- ✅ Portfolio-worthy project
- ✅ Professional development skills
- ✅ Experience with Python and C++

**Let's build something amazing! 🎮⚔️🐉**
