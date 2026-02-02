# Week 3 - RPG Game Exercises: Advanced Constructors and Destructors

## Exercise 1: Weapon with Resource Management
Create a `Weapon` class demonstrating constructors and destructors:

**Constructors:**
- Default constructor
- Parameterized constructor (name, damage, durability)
- Copy constructor (for weapon duplication)

**Destructor:**
- Display message when weapon is destroyed
- Track total active weapons

**Attributes:**
- `name`, `damage`, `durability`, `enchantment` (optional)

**Methods:**
- `attack()` - returns damage and reduces durability
- `is_usable()` - returns true if durability > 0
- `display_stats()`

**Tasks:**
1. Implement in both Python and C++
2. Create weapons using different constructors
3. Test copy constructor for weapon duplication
4. Observe destructor calls when objects go out of scope

## Exercise 2: Player with Complex Initialization
Create a `Player` class with multiple initialization options:

**Constructors:**
- Constructor with all parameters
- Constructor with default values for optional attributes
- Copy constructor (C++) or copy method (Python)

**Attributes:**
- Required: name, character_class
- Optional: level (default 1), health (default 100), mana (default 50)

**Methods:**
- `take_damage(amount)` - reduce health
- `heal(amount)` - increase health (max 100)
- `use_mana(amount)` - reduce mana if available
- `rest()` - restore health and mana to max

**Tasks:**
1. Implement constructors with different parameter combinations
2. Create players using various constructors
3. Test copy functionality

## Exercise 3: Quest with Destructor Patterns
Create a `Quest` class that manages resources:

**Attributes:**
- `quest_id`, `title`, `description`, `reward`, `is_active`

**Constructor:**
- Initialize all quest data
- Print "Quest accepted: [title]"

**Destructor:**
- Clean up quest resources
- Print "Quest completed/abandoned: [title]"

**Methods:**
- `complete()` - mark quest as completed and return reward
- `abandon()` - cancel the quest
- `display_info()`

**Tasks:**
1. Implement in both languages
2. Create quests in different scopes
3. Observe constructor/destructor call order
4. Test RAII pattern in C++ (Resource Acquisition Is Initialization)

See `solutions/` for reference implementations.
