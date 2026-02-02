# Week 6 - RPG Game Exercises: Multiple Inheritance

## Exercise 1: Special Character Abilities
Create a character with multiple inherited abilities:

**Mixin Classes:**

**`Flyable`**
- Method: `fly()` - move through air

**`Swimmable`**
- Method: `swim()` - move through water

**`Stealthy`**
- Method: `sneak()` - move undetected
- Method: `backstab()` - stealth attack

**Character Classes:**

**`Player`** (base character attributes)
- name, health, position

**`Rogue`** (inherits Player, Stealthy)
- Can sneak and backstab

**`Griffin`** (inherits Player, Flyable)
- Can fly

**`DragonRider`** (inherits Player, Flyable, Swimmable)
- Can both fly and swim

**Tasks:**
1. Implement mixin classes and character classes
2. Create different character types
3. Demonstrate multiple inheritance
4. Show Method Resolution Order (Python) or virtual inheritance (C++)

## Exercise 2: Hybrid Items
Create items with multiple inherited properties:

**Mixin Classes:**

**`Consumable`**
- `consume()` - use once and disappear
- `get_effect()` - return effect value

**`Equippable`**
- `equip()` - wear/wield the item
- `get_stat_bonus()` - return stat boost

**`Tradeable`**
- `get_value()` - return gold value
- `set_value(value)` - adjust price

**Hybrid Item Classes:**

**`EnchantedPotion`** (inherits Consumable, Tradeable)
- Can be consumed and sold

**`MagicArmor`** (inherits Equippable, Tradeable)
- Can be equipped and sold

**`TransformationScroll`** (inherits Consumable, Equippable)
- Can be consumed to gain temporary equipment effect

**Tasks:**
1. Implement all mixin and hybrid classes
2. Create instances of hybrid items
3. Use methods from all parent classes
4. Handle the diamond problem if it occurs

## Exercise 3: Enemy with Multiple Behaviors
Create complex enemy types with multiple abilities:

**Behavior Mixins:**

**`Aggressive`**
- `charge_attack()` - rush at player
- `get_aggro_range()` - return detection distance

**`Defensive`**
- `block()` - reduce incoming damage
- `retreat()` - move away when low health

**`Magical`**
- `cast_spell()` - use magic attack
- `get_mana()` - return current mana

**Enemy Classes:**

**`BasicEnemy`** (base class)
- name, health, damage

**`WarriorEnemy`** (inherits BasicEnemy, Aggressive, Defensive)
- Attacks aggressively but can defend

**`WizardEnemy`** (inherits BasicEnemy, Magical, Defensive)
- Casts spells and can defend

**`DragonBoss`** (inherits BasicEnemy, Aggressive, Magical, Flyable)
- Ultimate enemy with all abilities

**Tasks:**
1. Implement all behavior mixins and enemy classes
2. Create different enemy types
3. Demonstrate how DragonBoss uses all inherited abilities
4. Test combat scenarios with hybrid enemies

See `solutions/` for reference implementations.
