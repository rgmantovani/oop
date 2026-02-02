# Week 8 - RPG Game Exercises: Abstract Classes and Interfaces

## Exercise 1: Abstract Character System
Create an abstract character hierarchy:

**Abstract Class: `Character`**
- Abstract methods: `attack()`, `defend()`, `use_special_ability()`
- Concrete methods: `take_damage()`, `heal()`, `display_stats()`
- Attributes: name, health, max_health, level

**Concrete Classes:**

**`Knight`** (implements Character)
- Implement `attack()` - sword slash
- Implement `defend()` - shield block
- Implement `use_special_ability()` - heroic charge

**`Sorcerer`** (implements Character)
- Implement `attack()` - magic missile
- Implement `defend()` - magic shield
- Implement `use_special_ability()` - meteor storm

**`Rogue`** (implements Character)
- Implement `attack()` - dagger strike
- Implement `defend()` - dodge roll
- Implement `use_special_ability()` - shadow strike

**Tasks:**
1. Define abstract Character class (use ABC in Python, pure virtual in C++)
2. Implement all three character types
3. Attempt to instantiate Character directly (should fail)
4. Create combat using abstract interface

## Exercise 2: Item Interface System
Create item interfaces using abstract classes:

**Abstract Interface: `Usable`**
- Abstract method: `use(player)`

**Abstract Interface: `Droppable`**
- Abstract method: `drop()`
- Abstract method: `get_drop_location()`

**Abstract Interface: `Stackable`**
- Abstract method: `stack(amount)`
- Abstract method: `get_stack_size()`

**Concrete Classes:**

**`Potion`** (implements Usable, Stackable)
- Can be used and stacked

**`Weapon`** (implements Usable, Droppable)
- Can be used and dropped

**`Material`** (implements Stackable, Droppable)
- Can be stacked and dropped

**Tasks:**
1. Define abstract interfaces
2. Implement concrete classes with multiple interfaces
3. Create functions that accept interface types
4. Demonstrate interface segregation principle

## Exercise 3: Spell System with Abstract Base
Create an abstract spell system:

**Abstract Class: `Spell`**
- Attributes: name, mana_cost, cooldown, level_required
- Abstract methods: `cast(caster, target)`, `get_damage()`, `get_effect()`
- Concrete methods: `can_cast(player)`, `trigger_cooldown()`

**Concrete Spell Classes:**

**`DamageSpell`** (implements Spell)
- Implement `cast()` - deal damage to target
- Implement `get_damage()` - calculate damage
- Implement `get_effect()` - return "damage"

**`HealingSpell`** (implements Spell)
- Implement `cast()` - heal target
- Implement `get_damage()` - return 0
- Implement `get_effect()` - return "healing"

**`BuffSpell`** (implements Spell)
- Implement `cast()` - apply buff to target
- Implement `get_damage()` - return 0
- Implement `get_effect()` - return buff type

**Tasks:**
1. Create abstract Spell class
2. Implement all spell types
3. Create a Spellbook class that holds Spell objects
4. Cast different spells through common interface
5. Verify abstract class cannot be instantiated

See `solutions/` for reference implementations.
