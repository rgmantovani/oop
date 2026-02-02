# Week 10 - RPG Game Exercises: Exception Handling

## Exercise 1: Custom Game Exceptions
Create custom exception classes for game errors:

**Exception Classes:**

**`GameException`** (base exception)
- Base class for all game-related exceptions

**`InventoryFullException`** (inherits GameException)
- Raised when adding item to full inventory
- Store: attempted_item, current_capacity

**`InsufficientManaException`** (inherits GameException)
- Raised when casting spell without enough mana
- Store: required_mana, current_mana

**`InvalidActionException`** (inherits GameException)
- Raised when performing invalid action
- Store: action_name, reason

**`ItemNotFoundException`** (inherits GameException)
- Raised when item doesn't exist in inventory
- Store: item_name

**Tasks:**
1. Create all custom exception classes
2. Include meaningful error messages
3. Store relevant data in exceptions
4. Demonstrate exception hierarchy

## Exercise 2: Player with Exception Handling
Create a `Player` class with comprehensive error handling:

**Methods with Exception Handling:**

**`equip_weapon(weapon)`**
- Raise `ItemNotFoundException` if weapon not in inventory
- Raise `InvalidActionException` if weapon type not compatible
- Handle exceptions and provide feedback

**`cast_spell(spell, target)`**
- Raise `InsufficientManaException` if not enough mana
- Raise `InvalidActionException` if target invalid
- Use try-except-finally for cleanup

**`add_to_inventory(item)`**
- Raise `InventoryFullException` if no space
- Raise `ValueError` if item is None
- Ensure inventory state is consistent

**`use_item(item_name)`**
- Raise `ItemNotFoundException` if item not found
- Raise `InvalidActionException` if item not usable
- Remove item after successful use

**Tasks:**
1. Implement all methods with proper exception handling
2. Create test scenarios that trigger each exception
3. Use try-except-else-finally blocks appropriately
4. Demonstrate exception propagation

## Exercise 3: Combat System with Error Handling
Create a combat system with comprehensive exception handling:

**Classes:**

**`CombatSystem`**
- `initiate_combat(player, enemy)` - start combat
- `execute_action(action)` - perform combat action
- `end_combat()` - clean up combat state

**Exception Scenarios:**

1. **Combat Not Started**
   - Raise `InvalidActionException` when trying to attack before combat

2. **Dead Combatant**
   - Raise `InvalidActionException` when dead character tries to act

3. **Invalid Target**
   - Raise `InvalidActionException` for invalid targeting

4. **Spell/Ability Failure**
   - Handle multiple exception types (mana, cooldown, range)

**Tasks:**
1. Implement combat system with exception handling
2. Create comprehensive try-except blocks
3. Use exception chaining where appropriate
4. Provide helpful error messages to players
5. Ensure combat state remains valid after exceptions

## Bonus: Save/Load System with Exception Handling
Create a save/load system with file I/O exceptions:

**Methods:**
- `save_game(filename, player)` - save player state
- `load_game(filename)` - load player state

**Handle:**
- `FileNotFoundError` - save file doesn't exist
- `PermissionError` - cannot write to file
- `JSONDecodeError` / parsing errors - corrupted save file
- Custom `SaveGameException` - invalid game state

**Tasks:**
1. Implement save/load with exception handling
2. Test with missing files, corrupted data
3. Provide recovery options for failed loads
4. Use context managers for file operations

See `solutions/` for reference implementations.
