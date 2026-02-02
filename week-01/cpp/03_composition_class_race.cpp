/**
 * Week 1 - Composition: Player with Class and Race
 * Demonstrates the "HAS-A" relationship in C++
 */

#include <iostream>
#include <string>
#include <map>

using namespace std;

// CharacterClass represents a character class (Mage, Warrior, Thief, etc.)
class CharacterClass {
private:
    string name;
    string primaryStat;
    int startingHealth;
    int startingMana;

public:
    CharacterClass(string n, string stat, int health, int mana)
        : name(n), primaryStat(stat), startingHealth(health), startingMana(mana) {}
    
    string getName() const { return name; }
    string getPrimaryStat() const { return primaryStat; }
    int getStartingHealth() const { return startingHealth; }
    int getStartingMana() const { return startingMana; }
    
    map<string, int> getLevelBonus(int level) const {
        map<string, int> bonus;
        bonus["health"] = 10 * level;
        bonus["mana"] = 5 * level;
        return bonus;
    }
    
    void displayInfo() const {
        cout << "Class: " << name << endl;
        cout << "Primary Stat: " << primaryStat << endl;
        cout << "Starting HP: " << startingHealth << endl;
        cout << "Starting Mana: " << startingMana << endl;
    }
};

// Race represents a character race (Elf, Orc, Human, etc.)
class Race {
private:
    string name;
    int strengthBonus;
    int agilityBonus;
    int intelligenceBonus;
    string specialAbility;

public:
    Race(string n, int str, int agi, int intel, string ability)
        : name(n), strengthBonus(str), agilityBonus(agi), 
          intelligenceBonus(intel), specialAbility(ability) {}
    
    string getName() const { return name; }
    int getStrengthBonus() const { return strengthBonus; }
    int getAgilityBonus() const { return agilityBonus; }
    int getIntelligenceBonus() const { return intelligenceBonus; }
    string getSpecialAbility() const { return specialAbility; }
    
    map<string, int> getStatBonuses() const {
        map<string, int> bonuses;
        bonuses["strength"] = strengthBonus;
        bonuses["agility"] = agilityBonus;
        bonuses["intelligence"] = intelligenceBonus;
        return bonuses;
    }
    
    void displayInfo() const {
        cout << "Race: " << name << endl;
        cout << "Bonuses: STR +" << strengthBonus 
             << ", AGI +" << agilityBonus 
             << ", INT +" << intelligenceBonus << endl;
        cout << "Special Ability: " << specialAbility << endl;
    }
};

// Player class demonstrating composition with Class and Race
class Player {
private:
    string name;
    CharacterClass characterClass;  // Composition: Player HAS-A Class
    Race race;                       // Composition: Player HAS-A Race
    int level;
    int health;
    int maxHealth;
    int mana;
    int maxMana;
    int strength;
    int agility;
    int intelligence;

public:
    Player(string n, CharacterClass cClass, Race r, int lvl = 1)
        : name(n), characterClass(cClass), race(r), level(lvl) {
        
        // Calculate stats based on class and race
        maxHealth = characterClass.getStartingHealth();
        health = maxHealth;
        maxMana = characterClass.getStartingMana();
        mana = maxMana;
        
        // Apply racial bonuses
        strength = 10 + race.getStrengthBonus();
        agility = 10 + race.getAgilityBonus();
        intelligence = 10 + race.getIntelligenceBonus();
    }
    
    void displayInfo() const {
        cout << string(50, '=') << endl;
        cout << "Player: " << name << endl;
        cout << "Level: " << level << endl;
        cout << "Class: " << characterClass.getName() 
             << " (Primary: " << characterClass.getPrimaryStat() << ")" << endl;
        cout << "Race: " << race.getName() << endl;
        cout << "Health: " << health << "/" << maxHealth << endl;
        cout << "Mana: " << mana << "/" << maxMana << endl;
        cout << "Strength: " << strength << endl;
        cout << "Agility: " << agility << endl;
        cout << "Intelligence: " << intelligence << endl;
        cout << "Special Ability: " << race.getSpecialAbility() << endl;
        cout << string(50, '=') << endl;
    }
    
    void useRacialAbility() const {
        cout << name << " uses " << race.getSpecialAbility() << "!" << endl;
    }
    
    void levelUp() {
        level++;
        auto bonuses = characterClass.getLevelBonus(level);
        maxHealth += bonuses["health"];
        maxMana += bonuses["mana"];
        health = maxHealth;
        mana = maxMana;
        cout << name << " leveled up to " << level << "!" << endl;
    }
    
    int getHealth() const { return health; }
    int getMaxHealth() const { return maxHealth; }
    int getMana() const { return mana; }
    int getMaxMana() const { return maxMana; }
};

// Factory functions for creating classes and races
CharacterClass createWarriorClass() {
    return CharacterClass("Warrior", "Strength", 150, 30);
}

CharacterClass createMageClass() {
    return CharacterClass("Mage", "Intelligence", 80, 120);
}

CharacterClass createThiefClass() {
    return CharacterClass("Thief", "Agility", 100, 50);
}

Race createHumanRace() {
    return Race("Human", 2, 2, 2, "Adaptability (bonus XP)");
}

Race createElfRace() {
    return Race("Elf", 0, 5, 3, "Night Vision");
}

Race createOrcRace() {
    return Race("Orc", 6, 0, -2, "Berserker Rage");
}


int main() {
    cout << string(60, '=') << endl;
    cout << "CHARACTER CREATION - Composition Example" << endl;
    cout << string(60, '=') << endl;
    
    // Create character classes
    CharacterClass warriorClass = createWarriorClass();
    CharacterClass mageClass = createMageClass();
    CharacterClass thiefClass = createThiefClass();
    
    // Create races
    Race humanRace = createHumanRace();
    Race elfRace = createElfRace();
    Race orcRace = createOrcRace();
    
    // Create players with different combinations
    cout << "\n1. Human Warrior" << endl;
    Player player1("Thorin", warriorClass, humanRace);
    player1.displayInfo();
    
    cout << "\n2. Elf Mage" << endl;
    Player player2("Elandra", mageClass, elfRace);
    player2.displayInfo();
    
    cout << "\n3. Orc Warrior" << endl;
    Player player3("Grok", warriorClass, orcRace);
    player3.displayInfo();
    
    cout << "\n" << string(60, '=') << endl;
    cout << "DEMONSTRATING CLASS AND RACE METHODS" << endl;
    cout << string(60, '=') << endl;
    
    // Use racial abilities
    cout << "\nUsing Racial Abilities:" << endl;
    player1.useRacialAbility();
    player2.useRacialAbility();
    player3.useRacialAbility();
    
    // Level up
    cout << "\nLeveling Up:" << endl;
    player1.levelUp();
    cout << "New Stats: HP=" << player1.getHealth() << "/" << player1.getMaxHealth() 
         << ", Mana=" << player1.getMana() << "/" << player1.getMaxMana() << endl;
    
    // Display class info
    cout << "\nClass Information for Mage:" << endl;
    mageClass.displayInfo();
    
    // Display race info
    cout << "\nRace Information for Elf:" << endl;
    elfRace.displayInfo();
    
    return 0;
}
