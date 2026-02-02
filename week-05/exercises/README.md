# Week 5 - RPG Game Exercises: Single Inheritance

## Exercise 1: Item Hierarchy
Create an item inheritance system:

**Base Class: `Item`**
- Attributes: name, value, weight, description
- Methods: `display_info()`, `use()`, `__str__()`

**Derived Classes:**

**1. `Consumable` (inherits from Item)**
- Additional: effect_type ("healing", "mana", "buff"), effect_value
- Override `use()` - consume item and apply effect

**2. `Equipment` (inherits from Item)**
- Additional: slot ("head", "chest", "legs", "feet"), defense_bonus
- Override `use()` - equip item

**3. `QuestItem` (inherits from Item)**
- Additional: quest_id, is_key_item
- Override `use()` - display quest-related message

**Tasks:**
1. Implement base class and all derived classes
2. Create instances of each item type
3. Demonstrate method overriding
4. Test polymorphism by storing different items in a list

## Exercise 2: Character Class Hierarchy
Create a character inheritance system:

**Base Class: `Character`**
- Attributes: name, health, max_health, level, position_x, position_y
- Methods: `take_damage()`, `heal()`, `move()`, `is_alive()`, `display_stats()`

**Derived Classes:**

**1. `Player` (inherits from Character)**
- Additional: experience, inventory, equipped_weapon
- New methods: `gain_experience()`, `equip_weapon()`, `attack()`
- Override `display_stats()` to include player-specific info

**2. `Enemy` (inherits from Character)**
- Additional: enemy_type, reward_xp, reward_gold
- New methods: `attack_player()`, `drop_loot()`
- Override `display_stats()` to include enemy-specific info

**3. `NPC` (inherits from Character)**
- Additional: dialogue, quest_available
- New methods: `talk()`, `offer_quest()`

**Tasks:**
1. Implement the character hierarchy
2. Create players, enemies, and NPCs
3. Demonstrate that all inherit from Character
4. Test combat between Player and Enemy

## Exercise 3: Weapon Specialization
Create a weapon type hierarchy:

**Base Class: `Weapon`**
- Attributes: name, damage, durability, weapon_type
- Methods: `attack()`, `repair()`, `display_stats()`

**Derived Classes:**

**1. `MeleeWeapon` (inherits from Weapon)**
- Additional: range (short/medium), critical_chance
- Override `attack()` - melee attack with critical hit chance

**2. `RangedWeapon` (inherits from Weapon)**
- Additional: ammo_count, max_ammo, reload_time
- Override `attack()` - check ammo before attacking
- New method: `reload()`

**3. `MagicWeapon` (inherits from Weapon)**
- Additional: mana_cost, spell_type, spell_damage_bonus
- Override `attack()` - requires mana to use
- New method: `cast_spell()`

**Tasks:**
1. Implement all weapon types
2. Show how each weapon type has unique behavior
3. Create a combat scenario using different weapons
4. Demonstrate inheritance and method overriding

See `solutions/` for reference implementations.
