# Week 12 - RPG Game Exercises: Creational Design Patterns

## Exercise 1: Character Factory Pattern
Implement a factory to create different character types:

**CharacterFactory Class:**
- `create_character(class_name)` - factory method
- Returns appropriate character type based on class name

**Character Types:**
- `Warrior` - high health, low mana
- `Mage` - low health, high mana
- `Archer` - medium health, medium mana
- `Rogue` - low health, high agility

**Tasks:**
1. Implement CharacterFactory
2. Create characters using factory instead of direct instantiation
3. Add new character types easily through factory
4. Demonstrate benefits of factory pattern

## Exercise 2: Game Manager Singleton
Implement a game manager as a singleton:

**GameManager Class (Singleton):**
- Manages global game state
- Ensures only one instance exists

**Responsibilities:**
- Player management
- Quest tracking
- Game settings
- Global timers

**Methods:**
- `get_instance()` - return singleton instance
- `register_player(player)`
- `get_current_quest()`
- `update_game_time()`
- `save_global_state()`

**Tasks:**
1. Implement singleton pattern
2. Prevent multiple instances
3. Demonstrate global access to game manager
4. Test that all references point to same instance

## Exercise 3: Weapon Builder Pattern
Implement a builder for creating complex weapons:

**WeaponBuilder Class:**
- Fluent interface for building weapons step-by-step

**Building Steps:**
1. Set weapon type (sword, axe, bow, staff)
2. Set base damage
3. Add enchantments
4. Set rarity (common, rare, epic, legendary)
5. Add special effects
6. Build final weapon

**Example Usage:**
```python
weapon = (WeaponBuilder()
    .set_type("sword")
    .set_damage(50)
    .add_enchantment("fire", 15)
    .add_enchantment("lifesteal", 10)
    .set_rarity("epic")
    .add_effect("burn")
    .build())
```

**Tasks:**
1. Implement WeaponBuilder with fluent interface
2. Create Director class with preset weapon recipes
3. Build weapons step-by-step
4. Create "legendary" weapons with many properties

## Exercise 4: Item Prototype Pattern
Implement prototype pattern for item duplication:

**ItemPrototype Class:**
- `clone()` method to duplicate items
- Registry of prototype items

**Use Cases:**
1. Duplicate quest rewards
2. Create item stacks
3. Clone unique items with modifications

**ItemRegistry Class:**
- Stores prototype items
- `register_prototype(name, item)`
- `create_item(name)` - clone from prototype

**Tasks:**
1. Implement prototype pattern with clone method
2. Create item registry with common items
3. Clone items instead of creating from scratch
4. Modify cloned items independently
5. Demonstrate performance benefits

## Bonus: Abstract Factory for Game Themes
Create abstract factory for different game themes:

**Abstract Factory:**
- Creates families of related objects

**Themes:**
1. **Medieval Theme** - knights, swords, castles
2. **Sci-Fi Theme** - soldiers, laser guns, space stations
3. **Fantasy Theme** - wizards, magic staffs, towers

**Factories:**
- `MedievalFactory`
- `SciFiFactory`
- `FantasyFactory`

Each creates:
- Character type
- Weapon type
- Location type

**Tasks:**
1. Implement abstract factory pattern
2. Create theme-specific factories
3. Switch themes dynamically
4. Ensure consistency within theme

See `solutions/` for reference implementations.
