# Week 14 - RPG Game Exercises: Behavioral Design Patterns

## Exercise 1: Strategy Pattern for Combat AI
Implement different combat strategies:

**Strategy Interface: `CombatStrategy`**
- `execute_action(character, enemy)` - decide what action to take

**Concrete Strategies:**
- `AggressiveStrategy` - always attack with highest damage
- `DefensiveStrategy` - heal when low health, otherwise attack
- `BalancedStrategy` - mix of attack and defense
- `SupportStrategy` - buff allies, debuff enemies

**Enemy Class:**
- Has a combat strategy
- Can switch strategies based on health

**Tasks:**
1. Implement strategy interface and concrete strategies
2. Create enemies with different strategies
3. Switch strategy dynamically (e.g., defensive when low health)
4. Test combat with different AI behaviors

## Exercise 2: Observer Pattern for Event System
Implement event system using observer pattern:

**Subject: `Player`**
- Notifies observers of events

**Observers:**
- `QuestTracker` - updates quest progress
- `AchievementSystem` - unlocks achievements
- `StatisticsTracker` - records player stats
- `UIManager` - updates display

**Events to Track:**
- Enemy defeated
- Level up
- Item acquired
- Location entered
- Quest completed

**Tasks:**
1. Implement observer pattern
2. Register multiple observers to player
3. Trigger events and notify all observers
4. Demonstrate loose coupling between player and systems

## Exercise 3: Command Pattern for Action System
Implement command pattern for undoable actions:

**Command Interface:**
- `execute()` - perform action
- `undo()` - reverse action

**Concrete Commands:**
- `MoveCommand` - move player to new position
- `EquipWeaponCommand` - equip/unequip weapon
- `UseItemCommand` - use consumable item
- `DropItemCommand` - drop item from inventory

**CommandInvoker:**
- Executes commands
- Maintains history
- Supports undo/redo

**Tasks:**
1. Implement command interface and concrete commands
2. Create command invoker with history
3. Execute multiple commands
4. Implement undo functionality
5. Test redo capability

## Exercise 4: Template Method for Quest System
Implement template method for quest workflows:

**Abstract Class: `Quest`**
- Template method: `complete_quest()`
  1. `validate_objectives()` - abstract
  2. `calculate_rewards()` - abstract
  3. `grant_rewards()` - concrete
  4. `update_quest_log()` - concrete

**Concrete Quests:**
- `KillQuest` - defeat X enemies
  - Custom validation: check kill count
  - Custom rewards: based on enemy difficulty

- `CollectQuest` - gather X items
  - Custom validation: check inventory
  - Custom rewards: based on item rarity

- `DeliveryQuest` - deliver item to NPC
  - Custom validation: check location and item
  - Custom rewards: fixed gold/xp

**Tasks:**
1. Implement quest template method
2. Create concrete quest types
3. Complete different quests using same workflow
4. Demonstrate algorithm structure in base class

## Exercise 5: State Pattern for Player States
Implement state pattern for player state management:

**Player States:**
- `NormalState` - default state
- `CombatState` - during combat
- `StealthState` - sneaking
- `DeadState` - player is dead
- `RestingState` - recovering health/mana

**State Interface:**
- `handle_input(action)` - respond to player input
- `update()` - update state
- `enter_state()` - initialization
- `exit_state()` - cleanup

**State Behaviors:**
- Normal: can move, attack, use items
- Combat: can't rest, can flee
- Stealth: reduced movement, can backstab
- Dead: can only respawn
- Resting: health/mana regenerate, can't move

**Tasks:**
1. Implement state interface and concrete states
2. Create player with state management
3. Transition between states based on events
4. Show how behavior changes with state

## Bonus: Chain of Responsibility for Damage Processing
Implement chain of responsibility for damage calculation:

**Handlers:**
1. `ArmorHandler` - reduce damage by armor value
2. `BuffHandler` - apply buff modifiers
3. `ResistanceHandler` - apply elemental resistance
4. `CriticalHandler` - check for critical hit
5. `FinalDamageHandler` - apply final damage

**Tasks:**
1. Implement handler chain
2. Process damage through chain
3. Add/remove handlers dynamically
4. Log damage modifications at each step

See `solutions/` for reference implementations.
