# Week 1 - RPG Game Exercises

## Exercise 1: Create Player with Class and Race (Composition)
Create a Player class that uses **composition** with CharacterClass and Race objects:

**CharacterClass:**
- Attributes: name (string), primary_stat (string), starting_health (int), starting_mana (int)
- Methods: `get_level_bonus(level)`, `display_info()`

**Race:**
- Attributes: name (string), stat_bonuses (dict/map), special_ability (string)
- Methods: `get_stat_bonuses()`, `display_info()`

**Player:**
- Attributes: name (string), character_class (CharacterClass object), race (Race object), level (int)
- Calculated attributes: health, mana, stats (based on class and race)
- Methods: `display_info()`, `use_racial_ability()`, `level_up()`

**Available Classes:**
- Warrior: High HP (150), Low Mana (30), Primary Stat: Strength
- Mage: Low HP (80), High Mana (120), Primary Stat: Intelligence  
- Thief: Medium HP (100), Medium Mana (50), Primary Stat: Agility

**Available Races:**
- Human: Balanced bonuses (+2 all stats), Special: "Adaptability"
- Elf: Agility focus (+0 STR, +5 AGI, +3 INT), Special: "Night Vision"
- Orc: Strength focus (+6 STR, +0 AGI, -2 INT), Special: "Berserker Rage"

**Tasks:**
1. Implement CharacterClass, Race, and Player classes in Python
2. Implement CharacterClass, Race, and Player classes in C++
3. Create at least 3 players with different class/race combinations
4. Demonstrate composition (Player HAS-A Class, Player HAS-A Race)
5. Show how player stats are calculated from class and race

**Composition Key Points:**
- Player doesn't inherit from Class or Race
- Player contains Class and Race objects as attributes
- This is the "HAS-A" relationship (Player HAS-A Class, HAS-A Race)

## Exercise 2: Item with Enhanced Properties
Create an `Item` class to represent items in the game:

**Attributes:**
- name (string)
- item_type (string) - e.g., "Potion", "Weapon", "Armor"
- value (integer) - gold value
- weight (float) - item weight
- rarity (string) - "Common", "Rare", "Epic", "Legendary"

**Methods:**
- Constructor to initialize all attributes
- `display_info()` - show item details with rarity
- `is_heavy()` - returns true if weight > 10.0
- `get_value_per_weight()` - returns value divided by weight
- `get_sell_price()` - returns value * rarity multiplier

**Rarity Multipliers:**
- Common: 1.0x
- Rare: 1.5x
- Epic: 2.0x
- Legendary: 3.0x

**Tasks:**
1. Implement in both Python and C++
2. Create several items with different rarities
3. Test all methods and calculations
4. Sort items by value

## Exercise 3: Backpack with Capacity
Create a `Backpack` class for inventory management:

**Attributes:**
- owner_name (string)
- max_weight (float) - maximum weight capacity
- current_weight (float) - current weight of items
- items (list/vector of Item objects)

**Methods:**
- Constructor to initialize backpack
- `add_item(item)` - adds item if weight allows
- `remove_item(item_name)` - removes item from backpack
- `display_contents()` - shows all items with total weight
- `is_overweight()` - returns true if over capacity
- `get_total_value()` - sum of all item values

**Tasks:**
1. Implement in both Python and C++
2. Create a backpack with weight limit
3. Add items until capacity is reached
4. Try to add items when backpack is full and handle appropriately
5. Calculate total inventory value

## Bonus Challenge: Complete Character Creation
Create a character creation system:
- `CharacterCreator` class with menu system
- Let user choose:
  1. Character name
  2. Class (Warrior, Mage, Thief)
  3. Race (Human, Elf, Orc)
- Display final character stats
- Save character to file

**Advanced Features:**
- Class/race recommendations based on playstyle
- Stat preview before confirming
- Validation for choices

See the `solutions/` directory for reference implementations.
