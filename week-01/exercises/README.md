# Week 1 - RPG Game Exercises

## Exercise 1: Create Player with Class and Race (Composition)
Create a class `Player` to represent an RPG character:

**Attributes:**
- name (string)
- character_class (string) - e.g., "Warrior", "Mage", "Archer"
- level (integer)
- health (integer)

**Methods:**
- A constructor to initialize all attributes
- `display_info()` - displays all player information
- `is_alive()` - returns true if health > 0
- `level_up()` - increases level by 1 and health by 20

**Tasks:**
1. Implement the Player class in Python
2. Implement the Player class in C++
3. Create at least 3 different players with different classes
4. Test the level_up() method and display updated information

## Exercise 2: Item Class
Create a class `Item` to represent items in the game:

**Attributes:**
- name (string)
- item_type (string) - e.g., "Potion", "Weapon", "Armor"
- value (integer) - gold value
- weight (float) - item weight

**Methods:**
- Constructor to initialize all attributes
- `display_info()` - show item details
- `is_heavy()` - returns true if weight > 10.0
- `get_value_per_weight()` - returns value divided by weight

**Tasks:**
1. Implement in both Python and C++
2. Create several items with different types and weights
3. Test all methods

## Exercise 3: Simple Backpack Class
Create a simple `Backpack` class for inventory management:

**Attributes:**
- owner_name (string)
- max_capacity (integer) - maximum number of items
- items (list/vector of item names)

**Methods:**
- Constructor to initialize backpack
- `add_item(item_name)` - adds item if space available
- `remove_item(item_name)` - removes item from backpack
- `display_contents()` - shows all items
- `is_full()` - returns true if at capacity

**Tasks:**
1. Implement in both Python and C++
2. Create a backpack and add/remove items
3. Try to add items when backpack is full and handle appropriately

## Bonus Challenge: Basic Combat System
Create a simple combat system with:
- A `Weapon` class (name, damage, durability)
- An `Enemy` class (name, health, attack_power)
- A `combat()` function where player attacks enemy with weapon

See the `solutions/` directory for reference implementations.
