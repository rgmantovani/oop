# Week 9 - RPG Game Exercises: Operator Overloading and Special Methods

## Exercise 1: Position/Coordinate Class with Operators
Create a `Position` class with operator overloading:

**Attributes:**
- x, y (coordinates on game map)

**Operators to Overload:**

**Python:**
- `__add__` - add two positions (movement)
- `__sub__` - subtract positions (distance vector)
- `__eq__` - check if two positions are equal
- `__str__` - string representation
- `__repr__` - developer representation

**C++:**
- `operator+` - add positions
- `operator-` - subtract positions
- `operator==` - equality comparison
- `operator<<` - output stream

**Additional Methods:**
- `distance_to(other)` - calculate distance to another position
- `move(dx, dy)` - move by offset

**Tasks:**
1. Implement Position with all operators
2. Test position arithmetic (pos1 + pos2, pos1 - pos2)
3. Test equality comparison
4. Calculate distances between positions

## Exercise 2: Item Comparison and Arithmetic
Create an `Item` class with comparison operators:

**Attributes:**
- name, value, weight, rarity

**Operators to Overload:**

**Python:**
- `__lt__`, `__le__`, `__gt__`, `__ge__` - compare items by value
- `__eq__` - check if items are identical
- `__add__` - combine items (create bundle with total value)
- `__mul__` - duplicate item n times (stacking)
- `__str__` and `__repr__`

**C++:**
- `operator<`, `operator>`, `operator==` - comparisons
- `operator+` - combine items
- `operator*` - multiply item
- `operator<<` - output

**Tasks:**
1. Implement Item with all comparison operators
2. Sort items by value
3. Combine items using + operator
4. Stack items using * operator

## Exercise 3: Player Stats with Operator Overloading
Create a `Stats` class representing player statistics:

**Attributes:**
- strength, agility, intelligence, vitality

**Operators to Overload:**

**Python:**
- `__add__` - add stats (equipment bonuses)
- `__sub__` - subtract stats (debuffs)
- `__mul__` - multiply stats (buffs)
- `__iadd__`, `__isub__` - in-place modifications
- `__getitem__`, `__setitem__` - access stats by name
- `__str__` - display stats

**C++:**
- `operator+` - add stats
- `operator-` - subtract stats
- `operator*` - multiply stats
- `operator+=`, `operator-=` - compound assignment
- `operator[]` - subscript access
- `operator<<` - output

**Additional Methods:**
- `get_total()` - sum of all stats
- `apply_buff(multiplier)` - multiply all stats
- `copy()` - create a copy of stats

**Tasks:**
1. Implement Stats with all operators
2. Add equipment bonuses using + operator
3. Apply buff/debuff effects using * operator
4. Create player base stats and modified stats
5. Access individual stats using [] operator

See `solutions/` for reference implementations.
