"""
Week 1 - Composition: Player with Class and Race
Demonstrates the "HAS-A" relationship
"""

# Composition: Player HAS-A Class and HAS-A Race

class CharacterClass:
    """Represents a character class (Mage, Warrior, Thief, etc.)"""
    
    def __init__(self, name, primary_stat, starting_health, starting_mana):
        """
        Initialize character class
        
        Args:
            name: Class name (e.g., "Mage", "Warrior")
            primary_stat: Main attribute (e.g., "Intelligence", "Strength")
            starting_health: Base HP for this class
            starting_mana: Base mana for this class
        """
        self.name = name
        self.primary_stat = primary_stat
        self.starting_health = starting_health
        self.starting_mana = starting_mana
    
    def get_level_bonus(self, level):
        """Calculate bonus stats per level"""
        return {
            'health': 10 * level,
            'mana': 5 * level
        }
    
    def display_info(self):
        """Display class information"""
        print(f"Class: {self.name}")
        print(f"Primary Stat: {self.primary_stat}")
        print(f"Starting HP: {self.starting_health}")
        print(f"Starting Mana: {self.starting_mana}")
    
    def __str__(self):
        return self.name


class Race:
    """Represents a character race (Elf, Orc, Human, etc.)"""
    
    def __init__(self, name, strength_bonus, agility_bonus, intelligence_bonus, special_ability):
        """
        Initialize race
        
        Args:
            name: Race name (e.g., "Elf", "Orc", "Human")
            strength_bonus: Bonus to strength stat
            agility_bonus: Bonus to agility stat
            intelligence_bonus: Bonus to intelligence stat
            special_ability: Unique racial ability
        """
        self.name = name
        self.strength_bonus = strength_bonus
        self.agility_bonus = agility_bonus
        self.intelligence_bonus = intelligence_bonus
        self.special_ability = special_ability
    
    def get_stat_bonuses(self):
        """Return all stat bonuses as a dictionary"""
        return {
            'strength': self.strength_bonus,
            'agility': self.agility_bonus,
            'intelligence': self.intelligence_bonus
        }
    
    def display_info(self):
        """Display race information"""
        print(f"Race: {self.name}")
        print(f"Bonuses: STR +{self.strength_bonus}, AGI +{self.agility_bonus}, INT +{self.intelligence_bonus}")
        print(f"Special Ability: {self.special_ability}")
    
    def __str__(self):
        return self.name


class Player:
    """Player class demonstrating composition with Class and Race"""
    
    def __init__(self, name, character_class, race, level=1):
        """
        Initialize player with composition
        
        Args:
            name: Player's name
            character_class: CharacterClass object
            race: Race object
            level: Starting level
        """
        self.name = name
        self.character_class = character_class  # Composition: Player HAS-A Class
        self.race = race  # Composition: Player HAS-A Race
        self.level = level
        
        # Calculate stats based on class and race
        self.max_health = character_class.starting_health
        self.health = self.max_health
        self.max_mana = character_class.starting_mana
        self.mana = self.max_mana
        
        # Apply racial bonuses
        self.strength = 10 + race.strength_bonus
        self.agility = 10 + race.agility_bonus
        self.intelligence = 10 + race.intelligence_bonus
    
    def display_info(self):
        """Display complete player information"""
        print("=" * 50)
        print(f"Player: {self.name}")
        print(f"Level: {self.level}")
        print(f"Class: {self.character_class.name} (Primary: {self.character_class.primary_stat})")
        print(f"Race: {self.race.name}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Mana: {self.mana}/{self.max_mana}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Special Ability: {self.race.special_ability}")
        print("=" * 50)
    
    def use_racial_ability(self):
        """Use the racial special ability"""
        print(f"{self.name} uses {self.race.special_ability}!")
    
    def level_up(self):
        """Level up the player"""
        self.level += 1
        bonuses = self.character_class.get_level_bonus(self.level)
        self.max_health += bonuses['health']
        self.max_mana += bonuses['mana']
        self.health = self.max_health
        self.mana = self.max_mana
        print(f"{self.name} leveled up to {self.level}!")


# Factory functions for creating classes and races
def create_warrior_class():
    """Factory function for Warrior class"""
    return CharacterClass(
        name="Warrior",
        primary_stat="Strength",
        starting_health=150,
        starting_mana=30
    )

def create_mage_class():
    """Factory function for Mage class"""
    return CharacterClass(
        name="Mage",
        primary_stat="Intelligence",
        starting_health=80,
        starting_mana=120
    )

def create_thief_class():
    """Factory function for Thief class"""
    return CharacterClass(
        name="Thief",
        primary_stat="Agility",
        starting_health=100,
        starting_mana=50
    )


def create_human_race():
    """Factory function for Human race"""
    return Race(
        name="Human",
        strength_bonus=2,
        agility_bonus=2,
        intelligence_bonus=2,
        special_ability="Adaptability (bonus XP)"
    )

def create_elf_race():
    """Factory function for Elf race"""
    return Race(
        name="Elf",
        strength_bonus=0,
        agility_bonus=5,
        intelligence_bonus=3,
        special_ability="Night Vision"
    )

def create_orc_race():
    """Factory function for Orc race"""
    return Race(
        name="Orc",
        strength_bonus=6,
        agility_bonus=0,
        intelligence_bonus=-2,
        special_ability="Berserker Rage"
    )


if __name__ == "__main__":
    print("=" * 60)
    print("CHARACTER CREATION - Composition Example")
    print("=" * 60)
    
    # Create character classes
    warrior_class = create_warrior_class()
    mage_class = create_mage_class()
    thief_class = create_thief_class()
    
    # Create races
    human_race = create_human_race()
    elf_race = create_elf_race()
    orc_race = create_orc_race()
    
    # Create players with different combinations
    print("\n1. Human Warrior")
    player1 = Player("Thorin", warrior_class, human_race)
    player1.display_info()
    
    print("\n2. Elf Mage")
    player2 = Player("Elandra", mage_class, elf_race)
    player2.display_info()
    
    print("\n3. Orc Warrior")
    player3 = Player("Grok", warrior_class, orc_race)
    player3.display_info()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATING CLASS AND RACE METHODS")
    print("=" * 60)
    
    # Use racial abilities
    print("\nUsing Racial Abilities:")
    player1.use_racial_ability()
    player2.use_racial_ability()
    player3.use_racial_ability()
    
    # Level up
    print("\nLeveling Up:")
    player1.level_up()
    print(f"New Stats: HP={player1.health}/{player1.max_health}, Mana={player1.mana}/{player1.max_mana}")
    
    # Display class info
    print("\nClass Information for Mage:")
    mage_class.display_info()
    
    # Display race info
    print("\nRace Information for Elf:")
    elf_race.display_info()
