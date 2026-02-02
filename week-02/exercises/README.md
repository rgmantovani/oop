# Week 2 - RPG Game Exercises: Class Variables and Constructors

## Exercise 1: Player Registry System
Create a `Player` class with class and instance variables:

**Class Variables:**
- `game_name` (shared by all players) - e.g., "Epic Quest RPG"
- `total_players` (count of all players created)

**Instance Variables:**
- `player_id` (auto-generated from total_players)
- `name`
- `experience_points` (list/array of XP gains)

**Methods:**
- Constructor to initialize player
- `gain_experience(xp)` - add XP to the list
- `get_total_xp()` - return sum of all experience points
- `get_level()` - return level based on total XP (level = total_xp // 100)
- `display_info()` - show player information
- Class method `get_total_players()`

**Tasks:**
1. Implement in both Python and C++
2. Create multiple players
3. Add experience points and check level progression
4. Display total player count

## Exercise 2: Weapon Inventory System
Create a `Weapon` class with:

**Instance Variables:**
- `name`, `damage`, `weapon_type`, `durability`

**Class Variables:**
- `total_weapons` - count of all weapon objects
- `smithy_name` - shared forge name

**Methods:**
- Constructor
- `use()` - decrease durability by 1 (if durability > 0)
- `repair(amount)` - increase durability
- `is_broken()` - check if durability <= 0
- `display_info()`

**Tasks:**
1. Implement in both languages
2. Test using and repairing weapons
3. Handle cases where weapon is broken

## Exercise 3: Item Class with Multiple Constructors
Create an `Item` class with comprehensive initialization:

**Constructors (C++):**
- Default constructor (name="Unknown", value=0, weight=1.0)
- Parameterized constructor (custom values)
- Copy constructor

**Python:**
- Constructor with default parameters

**Methods:**
- `display_info()` - show item details
- `apply_bonus(multiplier)` - multiply value by multiplier
- `combine_with(other_item)` - create new item with combined properties

**Tasks:**
1. Implement in both languages
2. Test all constructor types
3. Test item combination

See `solutions/` for reference implementations.
