# Week 11 - RPG Game Exercises: File I/O and Serialization

## Exercise 1: Save/Load Player Data
Create a system to persist player data:

**Player Class:**
- Attributes: name, level, health, mana, experience, gold, position

**Requirements:**
1. Implement `save_to_file(filename)` method
2. Implement `load_from_file(filename)` class method
3. Support both JSON and binary formats

**File Formats:**

**JSON Format:**
```json
{
  "name": "Hero",
  "level": 10,
  "health": 85,
  "mana": 60,
  "experience": 1250,
  "gold": 500,
  "position": {"x": 100, "y": 200}
}
```

**Tasks:**
1. Implement JSON serialization/deserialization
2. Implement binary serialization (pickle in Python, custom in C++)
3. Test saving and loading player state
4. Handle file errors gracefully

## Exercise 2: Inventory Persistence
Create an inventory system with file persistence:

**Inventory Class:**
- List of items with all properties

**Requirements:**
1. Save inventory to CSV file
2. Load inventory from CSV file
3. Export inventory report to text file

**CSV Format:**
```csv
name,type,value,weight,quantity
Health Potion,consumable,50,0.5,10
Iron Sword,weapon,200,5.0,1
```

**Tasks:**
1. Implement CSV export for inventory
2. Implement CSV import to reconstruct inventory
3. Generate human-readable inventory report
4. Handle invalid CSV data

## Exercise 3: Quest Log System
Create a quest tracking system with persistence:

**Quest Class:**
- quest_id, title, description, status, objectives, rewards

**QuestLog Class:**
- List of quests
- Methods to add, update, complete quests

**Requirements:**
1. Save quest log to JSON file
2. Load quest log from file
3. Export quest log to formatted text report
4. Track quest history

**JSON Format:**
```json
{
  "quests": [
    {
      "quest_id": "Q001",
      "title": "Defeat the Dragon",
      "description": "...",
      "status": "in_progress",
      "objectives": [
        {"desc": "Find the dragon", "completed": true},
        {"desc": "Defeat the dragon", "completed": false}
      ],
      "rewards": {"xp": 1000, "gold": 500}
    }
  ]
}
```

**Tasks:**
1. Implement complete quest serialization
2. Handle nested data structures (objectives, rewards)
3. Generate quest completion report
4. Implement auto-save on quest status changes

## Bonus: Game World State Serialization
Create a complete game state save system:

**GameState Class:**
- player data
- inventory
- quest log
- game settings
- visited locations

**Requirements:**
1. Save entire game state to single file
2. Load complete game state
3. Implement checkpoint system (multiple saves)
4. Create backup saves automatically

**Tasks:**
1. Serialize complex nested objects
2. Implement versioning for save files
3. Handle save file corruption
4. Create save file manager with multiple slots

See `solutions/` for reference implementations.
