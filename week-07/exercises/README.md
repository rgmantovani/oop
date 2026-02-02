# Week 7 - RPG Game Exercises: Polymorphism and Method Overriding

## Exercise 1: Polymorphic Combat System
Create a combat system using polymorphism:

**Base Class: `Combatant`**
- Attributes: name, health, defense
- Methods: `attack()`, `take_damage(amount)`, `is_alive()`

**Derived Classes:**

**`Warrior`**
- Override `attack()` - returns high physical damage
- Special: power_strike() - extra damage with cooldown

**`Mage`**
- Override `attack()` - returns magic damage
- Special: fireball() - area damage spell

**`Archer`**
- Override `attack()` - returns ranged damage
- Special: arrow_rain() - multiple hits

**Tasks:**
1. Implement base class and all derived classes
2. Create a function `battle(combatant1, combatant2)` that works with any Combatant
3. Demonstrate polymorphism by calling attack() on different types
4. Create a tournament with mixed character types

## Exercise 2: Item Usage Polymorphism
Create polymorphic item usage:

**Base Class: `UsableItem`**
- Attributes: name, description
- Method: `use(player)` - abstract/virtual

**Derived Classes:**

**`HealthPotion`**
- Override `use(player)` - restore player health

**`ManaPotion`**
- Override `use(player)` - restore player mana

**`StrengthBuff`**
- Override `use(player)` - temporarily increase player damage

**`TeleportScroll`**
- Override `use(player)` - move player to safe location

**Tasks:**
1. Implement all item types
2. Create a `use_item(item, player)` function that works polymorphically
3. Store different items in a single collection
4. Iterate and use items showing polymorphic behavior

## Exercise 3: Quest Reward System
Create a polymorphic reward system:

**Base Class: `Reward`**
- Method: `grant(player)` - abstract/virtual
- Method: `describe()` - show reward description

**Derived Classes:**

**`GoldReward`**
- Override `grant(player)` - add gold to player
- Override `describe()` - show gold amount

**`ExperienceReward`**
- Override `grant(player)` - add XP to player
- Override `describe()` - show XP amount

**`ItemReward`**
- Override `grant(player)` - add item to inventory
- Override `describe()` - show item details

**`SkillReward`**
- Override `grant(player)` - unlock new skill
- Override `describe()` - show skill name

**Tasks:**
1. Implement all reward types
2. Create a Quest class that has a list of rewards
3. Complete quest and grant all rewards polymorphically
4. Show that same interface works for different reward types

See `solutions/` for reference implementations.
