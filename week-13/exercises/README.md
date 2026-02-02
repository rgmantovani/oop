# Week 13 - RPG Game Exercises: Structural Design Patterns

## Exercise 1: Item Decorator Pattern
Implement decorator pattern for item enhancement:

**Base: `Weapon`**
- Basic weapon with damage

**Decorators:**
- `FireEnchantment` - adds fire damage
- `IceEnchantment` - adds ice damage
- `PoisonEnchantment` - adds poison damage
- `CriticalEnhancement` - adds critical hit chance
- `DurabilityEnhancement` - increases durability

**Requirements:**
1. Decorators wrap weapons and add properties
2. Multiple decorators can be stacked
3. Calculate total damage including all enchantments

**Example:**
```python
weapon = Weapon("Sword", 50)
weapon = FireEnchantment(weapon, 15)
weapon = CriticalEnhancement(weapon, 0.2)
# Sword with 50 base + 15 fire damage + 20% crit
```

**Tasks:**
1. Implement base Weapon class
2. Create multiple decorator classes
3. Stack decorators on weapons
4. Calculate enhanced stats dynamically

## Exercise 2: Adapter Pattern for Legacy Items
Create adapters for integrating old item system:

**Legacy System:**
- Old items use different interface
- Methods: `getValue()`, `getWeight()`, `getName()`

**New System:**
- New items use: `get_value()`, `get_weight()`, `get_name()`
- Different data structures

**Adapter:**
- `LegacyItemAdapter` - makes legacy items work with new system

**Tasks:**
1. Create legacy item class (old style)
2. Create new item class (new style)
3. Implement adapter to bridge them
4. Use both types in same inventory

## Exercise 3: Facade Pattern for Combat System
Create a simplified interface for complex combat:

**Complex Subsystems:**
- `DamageCalculator` - calculates damage with formulas
- `BuffManager` - manages active buffs/debuffs
- `AnimationSystem` - handles combat animations
- `SoundManager` - plays combat sounds
- `StatisticsTracker` - tracks combat stats

**CombatFacade:**
- `attack(attacker, defender)` - simple attack interface
- Internally coordinates all subsystems

**Tasks:**
1. Implement all subsystem classes
2. Create CombatFacade that uses them
3. Simplify combat to single method calls
4. Hide complexity from client code

## Exercise 4: Composite Pattern for Inventory
Implement composite pattern for nested inventory:

**Component Interface: `InventoryComponent`**
- `add_item()`, `remove_item()`, `get_total_value()`, `display()`

**Leaf: `Item`**
- Single item (weapon, potion, etc.)

**Composite: `Container`**
- Can hold items and other containers
- Examples: Backpack, Chest, Bag

**Structure:**
```
Backpack (composite)
├── Weapon (leaf)
├── Small Bag (composite)
│   ├── Potion (leaf)
│   └── Potion (leaf)
└── Gold (leaf)
```

**Tasks:**
1. Implement component interface
2. Create leaf (Item) and composite (Container) classes
3. Build nested inventory structure
4. Calculate total value recursively
5. Display inventory tree

## Exercise 5: Proxy Pattern for Lazy Loading
Implement proxy for loading large game assets:

**Real Object: `GameAsset`**
- Large object (textures, models, audio)
- Expensive to load

**Proxy: `GameAssetProxy`**
- Lightweight placeholder
- Loads real asset only when needed (lazy loading)
- Caches loaded asset

**Use Cases:**
1. Player textures - load only when player enters area
2. Sound effects - load only when about to play
3. Item models - load only when displayed

**Tasks:**
1. Create GameAsset class (simulate expensive loading)
2. Implement GameAssetProxy with lazy loading
3. Demonstrate loading on first access only
4. Show performance improvement

## Bonus: Bridge Pattern for Rendering
Separate abstraction from implementation for rendering:

**Abstraction: `Character`**
- High-level character operations

**Implementation: `Renderer`**
- Different rendering backends:
  - `ConsoleRenderer` - text-based
  - `GraphicsRenderer` - graphical
  - `DebugRenderer` - wireframe

**Tasks:**
1. Implement bridge pattern
2. Switch renderers at runtime
3. Add new renderer without changing Character
4. Demonstrate independence of abstraction and implementation

See `solutions/` for reference implementations.
