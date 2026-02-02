# Incremental RPG Development Guide

## Overview

This course uses an **incremental development** approach where you build a single RPG system over 15 weeks. Each week introduces new OOP concepts that you apply to expand your game.

## Development Philosophy

Instead of isolated exercises, you'll:
- ✅ Build one cohesive RPG game
- ✅ Add features each week using new concepts
- ✅ Refactor and improve previous code
- ✅ See how real applications grow over time
- ✅ Experience continuous integration of new features

## Weekly Development Roadmap

### Week 1: Foundation - Core Entities
**What You'll Build:**
- `Player` class (name, class, level, health)
- `Item` class (name, type, value, weight)
- `Backpack` class (basic inventory)
- Simple display methods

**Files to Create:**
- `player.py` / `Player.cpp`
- `item.py` / `Item.cpp`
- `backpack.py` / `Backpack.cpp`
- `main.py` / `main.cpp`

**Milestone:** Can create a player and add items to backpack

---

### Week 2: Class Variables and State
**What You'll Add:**
- Player registry (track all players with class variables)
- Weapon class with durability system
- Experience point tracking
- Constructor variations

**New Features:**
- Track total players created
- Weapons that degrade with use
- Level calculation based on XP
- Multiple initialization methods

**Milestone:** Players gain XP, level up, and weapons can break

---

### Week 3: Resource Management
**What You'll Add:**
- Quest system with lifecycle
- Weapon copying/duplication
- Resource cleanup (destructors)
- Memory management patterns

**New Features:**
- Accept and complete quests
- Duplicate legendary weapons
- Proper object cleanup
- Track active objects

**Milestone:** Complete quest system with rewards

---

### Week 4: Encapsulation & Data Protection
**What You'll Refactor:**
- Make player stats private with validation
- Add getters/setters with bounds checking
- Protect backpack from invalid operations
- Encapsulate weapon enchantments

**New Features:**
- Stats can't go below 0 or above max
- Property decorators (Python) for clean access
- Validated inventory operations
- Protected enchantment levels

**Milestone:** Robust system that prevents invalid states

---

### Week 5: Character Hierarchy
**What You'll Add:**
- Abstract `Character` base class
- `Player`, `Enemy`, `NPC` derived classes
- `Item` hierarchy: `Consumable`, `Equipment`, `QuestItem`
- `Weapon` specializations: `MeleeWeapon`, `RangedWeapon`, `MagicWeapon`

**New Features:**
- All characters share common behavior
- Items have type-specific functionality
- Different weapon types work differently
- Method overriding for specialized behavior

**Milestone:** Fight enemies with different weapon types

---

### Week 6: Multiple Inheritance & Abilities
**What You'll Add:**
- Ability mixins: `Flyable`, `Swimmable`, `Stealthy`
- Hybrid characters: `DragonRider`, `Rogue`
- Hybrid items: `EnchantedPotion`, `MagicArmor`
- Complex enemy types

**New Features:**
- Characters with multiple special abilities
- Items that combine properties
- Enemies with mixed behaviors
- Diamond problem solutions

**Milestone:** Special character classes with unique ability combinations

---

### Week 7: Polymorphic Combat
**What You'll Add:**
- Combat system that works with any character
- Polymorphic item usage
- Quest reward system with multiple reward types
- Dynamic ability execution

**New Features:**
- `battle(char1, char2)` works with any character type
- Items used through common interface
- Rewards granted polymorphically
- Method overriding in action

**Milestone:** Full combat system with any character types

---

### Week 8: Abstract Systems & Interfaces
**What You'll Add:**
- Abstract spell system
- Item interfaces (Usable, Droppable, Stackable)
- Abstract quest template
- Pure virtual methods

**New Features:**
- Spell hierarchy with different spell types
- Interface-based item design
- Cannot instantiate abstract classes
- Contract-based programming

**Milestone:** Spellcasting system with multiple spell schools

---

### Week 9: Operator Overloading
**What You'll Add:**
- `Position` class with arithmetic operators
- Item comparison operators
- `Stats` class with operator overloading
- Natural syntax for game operations

**New Features:**
- `pos1 + pos2` for movement
- `item1 > item2` for comparisons
- `stats1 + stats2` for equipment bonuses
- Intuitive item stacking

**Milestone:** Natural mathematical operations on game entities

---

### Week 10: Exception Handling
**What You'll Add:**
- Custom exception hierarchy
- Robust error handling in all systems
- Safe combat system
- Validated operations everywhere

**New Features:**
- `InventoryFullException`, `InsufficientManaException`, etc.
- Try-catch blocks in critical code
- Graceful error recovery
- Meaningful error messages

**Milestone:** Game doesn't crash, handles all errors gracefully

---

### Week 11: Persistence & Saving
**What You'll Add:**
- Save/load player data
- Inventory persistence
- Quest log serialization
- Complete game state saving

**New Features:**
- Save game to JSON/binary
- Load game from file
- Auto-save functionality
- Multiple save slots

**Milestone:** Complete save/load system

---

### Week 12: Creational Patterns
**What You'll Add:**
- Singleton `GameManager`
- `CharacterFactory` for creating characters
- `WeaponBuilder` for complex weapons
- Item prototype registry

**New Features:**
- Global game state management
- Easy character creation
- Fluent weapon building
- Clone items efficiently

**Milestone:** Professional object creation patterns

---

### Week 13: Structural Patterns
**What You'll Add:**
- Decorator for item enchantments
- Adapter for legacy items
- Facade for combat system
- Composite for nested inventory
- Proxy for lazy asset loading

**New Features:**
- Stack enchantments on items
- Simplified combat interface
- Containers within containers
- Performance optimization

**Milestone:** Clean, maintainable system architecture

---

### Week 14: Behavioral Patterns
**What You'll Add:**
- Strategy for enemy AI
- Observer for event system
- Command for undo/redo
- Template method for quest workflows
- State for player states

**New Features:**
- Intelligent enemy behavior
- Achievement system
- Undo player actions
- Different quest types
- State-based player behavior

**Milestone:** Sophisticated game behavior and AI

---

### Week 15: Integration & Polish
**What You'll Complete:**
- Main game loop
- Complete UI/menu system
- Game content (areas, enemies, quests)
- Final testing and polish
- Documentation

**Final Features:**
- Playable from start to finish
- Multiple areas to explore
- Complete quest lines
- Save/load functionality
- Professional documentation

**Milestone:** Complete, playable RPG game!

---

## File Organization Strategy

### Start Simple (Weeks 1-3)
```
rpg-game/
├── python/
│   ├── player.py
│   ├── item.py
│   ├── backpack.py
│   └── main.py
```

### Organize by Feature (Weeks 4-8)
```
rpg-game/
├── python/
│   ├── characters/
│   ├── items/
│   ├── inventory/
│   └── main.py
```

### Full Architecture (Weeks 9-15)
```
rpg-game/
├── python/
│   ├── core/
│   ├── characters/
│   ├── items/
│   ├── combat/
│   ├── quests/
│   ├── world/
│   ├── persistence/
│   ├── exceptions/
│   └── main.py
```

## Git Workflow

### Branching Strategy
```bash
main (stable)
├── week-01-foundation
├── week-02-constructors
├── week-03-destructors
└── ...
```

### Commit After Each Milestone
```bash
git add .
git commit -m "Week 3: Add quest system with lifecycle management"
git push origin week-03-destructors
```

## Testing Strategy

### Progressive Testing
- **Weeks 1-5:** Manual testing
- **Weeks 6-10:** Add basic unit tests
- **Weeks 11-15:** Comprehensive test suite

### What to Test Each Week
1. New features added this week
2. Integration with previous features
3. Edge cases and error conditions

## Refactoring Guidelines

### When to Refactor
- Code becomes too complex
- Duplication appears
- New pattern would simplify design
- Better solution becomes apparent

### What to Refactor
- Extract common code to base classes
- Apply design patterns learned
- Improve naming and organization
- Enhance error handling

## Tips for Success

### 1. Version Control Everything
```bash
# After each major milestone
git add .
git commit -m "Descriptive message about what you added"
```

### 2. Test Before Moving On
Don't start a new week until the current week's code works properly.

### 3. Keep Notes
Document design decisions and why you made certain choices.

### 4. Refactor Freely
Early code will be simple. That's okay! Refactor it when you learn better approaches.

### 5. Build Both Versions
Keep Python and C++ implementations in sync to understand language differences.

### 6. Play Your Game
Regularly play your own game to find bugs and usability issues.

### 7. Show Your Work
Share progress with classmates for feedback and ideas.

## Common Challenges & Solutions

### Challenge 1: Code Getting Messy
**Solution:** Refactor regularly. Split large files into smaller ones.

### Challenge 2: Forgetting Previous Code
**Solution:** Review previous weeks before starting new one.

### Challenge 3: Conflicts Between Features
**Solution:** Plan integration before implementing.

### Challenge 4: Bugs from Weeks Ago
**Solution:** Write tests as you go. Fix bugs immediately.

### Challenge 5: Lost Motivation
**Solution:** Focus on making something fun. Show friends. Take breaks.

## Progress Tracking

### Weekly Checklist
After each week, ensure:
- [ ] All exercises completed
- [ ] Code tested and working
- [ ] Integrated with previous weeks
- [ ] Committed to version control
- [ ] Documentation updated
- [ ] Python and C++ in sync

## Milestone Demonstrations

### Mid-Term Demo (Week 7)
Show:
- Character creation
- Inventory management
- Basic combat
- Quest system

### Final Demo (Week 15)
Show:
- Complete gameplay loop
- All features integrated
- Save/load working
- Polished experience

## Resources

### When You're Stuck
1. Review the week's README
2. Check example code
3. Review previous weeks
4. Ask classmates
5. Search documentation
6. Ask instructor

### Inspiration
- Play other RPGs for ideas
- Think about what would be fun
- Draw inspiration from your favorite games
- Keep it simple but engaging

## Remember

This is YOUR RPG. While the exercises provide structure:
- Add your own creative touches
- Extend beyond requirements
- Make it fun and unique
- Take pride in your creation

By Week 15, you'll have built a complete RPG game demonstrating professional OOP practices. This is a portfolio piece you can showcase!

**Happy Coding! 🎮⚔️🐉**
