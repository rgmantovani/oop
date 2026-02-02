# Week 4 - RPG Game Exercises: Encapsulation and Access Control

## Exercise 1: Player with Encapsulated Stats
Create a `Player` class with proper encapsulation:

**Private Attributes:**
- `__name`, `__health`, `__max_health`, `__mana`, `__max_mana`, `__level`, `__experience`

**Public Methods (Getters):**
- `get_name()`, `get_health()`, `get_max_health()`, `get_level()`

**Public Methods (Setters with Validation):**
- `set_health(value)` - ensure 0 <= health <= max_health
- `set_mana(value)` - ensure 0 <= mana <= max_mana

**Public Methods (Business Logic):**
- `take_damage(amount)` - reduce health, prevent going below 0
- `heal(amount)` - increase health, not exceeding max
- `gain_experience(xp)` - add XP, level up if threshold reached
- `display_stats()`

**Python Bonus:**
- Use @property decorators for health, mana, level

**Tasks:**
1. Implement with proper encapsulation in both languages
2. Demonstrate that private attributes cannot be accessed directly
3. Test validation in setters (try invalid values)
4. Test automatic level-up system

## Exercise 2: Backpack with Item Management
Create an encapsulated `Backpack` class:

**Private Attributes:**
- `__items` (list of Item objects)
- `__max_weight_capacity`
- `__current_weight`
- `__max_slots`

**Public Methods:**
- `add_item(item)` - validate weight and slots before adding
- `remove_item(item_name)` - remove and return item
- `get_item(item_name)` - return item without removing
- `get_total_weight()` - return current weight
- `get_available_slots()` - return remaining slots
- `display_contents()`

**Validation Rules:**
- Cannot exceed max_weight_capacity
- Cannot exceed max_slots
- Cannot add duplicate items with same name

**Tasks:**
1. Implement with encapsulation
2. Test weight and slot limits
3. Try to access private attributes directly (should fail)
4. Implement proper error messages for failed operations

## Exercise 3: Weapon with Enchantment Protection
Create a `Weapon` class with protected enchantment system:

**Private Attributes:**
- `__name`, `__base_damage`, `__durability`, `__max_durability`
- `__enchantment_level` (0-5)
- `__is_enchantable`

**Public Methods:**
- `get_total_damage()` - returns base_damage + (enchantment_level * 10)
- `use()` - reduce durability, return total damage
- `repair(amount)` - restore durability
- `enchant()` - increase enchantment level if allowed

**Private Helper Methods:**
- `__calculate_damage()` - internal damage calculation
- `__validate_enchantment()` - check if weapon can be enchanted

**Tasks:**
1. Implement proper encapsulation
2. Demonstrate private helper methods
3. Show that enchantment level cannot be modified directly
4. Create getters without setters for read-only properties

See `solutions/` for reference implementations.
