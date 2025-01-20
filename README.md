# Rule_Based_AI_System_CAP320


# Part 1: Initial Project Ideas

## 1. Project Idea 1: Game AI
  - **Concept:** Create AI for a simple game using rules for decision-making.
  - **Example:** AI for a tic-tac-toe game that makes moves based on heuristics like "block opponent’s win" or "maximize chances to win."
  - **Features:**
    - Rules for evaluating board positions.
    - Turn-based logic for gameplay.

## 2. Project Idea 2: Rule-Based Calculator
  - **Concept:** Solve specific problems using rules, such as tax calculations or unit conversions.
  - **Example:** A rule-based tax calculator for determining deductions and total taxes based on income brackets.
  - **Features:**
    - Rules for different conditions (e.g., income range, deductions).
    - User input for customization.

## 3. Project Idea 3: Character Creator for RPGs
  - **Concept:** A helper for creating role-playing game characters with rule constraints.
  - **Example:** Input choices for race, class, and abilities, and the system checks alignment with D&D rules.
  - **Features:**
    - Rules for valid combinations (e.g., "Clerics must have wisdom ≥ 13").
    - Suggestions for unassigned stats or traits.
    - Basic output with character sheet details.

### Chosen Idea: Character Creator for D&D 5e (Dungeons & Dragons 5th Edition)

**Justification:** I chose this project because I am already familiar with the rules so I can help guide the coding. It also includes all the requirements of the assignment including user input for character choices, conditional logic to ensure those choices match the game rules, and output of errors or user choices based on that logic.

## Part 2: Rules/Logic for the Chosen System
The D&D Character Creator system will follow these rules:

  ### 1. Race Selection:
    - The system will show all available races. You must type in one from the list.
    - If a race includes any sub-races then the system will display them for you to pick from (e.g., "High Elf" vs. "Wood Elf").
    - Each race has unique bonuses (e.g., "+2 Dexterity for Elves").
    - Racial features (e.g., "Darkvision" for Dwarves).

  ### 2. Class Selection:
    - The system will show all available classes. You must type in one from the list.
    - Each class has specific hit dice (e.g., d10 for Fighters).
    - Each class has different starting proficiencies (weapons, armor, skills).
    - Class features (e.g., "Rage" for Barbarians).

  ### 3. Ability Scores:
    - This system will only use the point buy method
      - Starting with a stat of 8 costs nothing.
      - A stat of 9 costs 1 point
      - A stat of 10 costs 2 points
      - A stat of 11 costs 3 points
      - A stat of 12 costs 4 points
      - A stat of 13 costs 5 points
      - A stat of 14 costs 7 points
      - A stat of 15 costs 9 points
      - You can not purchase a stat above 15 using the point buy method. 
    - Ensure all ability scores are valid (e.g., 8–15 before racial bonuses with point buy).
    - Display points left after selecting each score.
    - Apply racial bonuses after base scores.
    - Calculate modifiers for each ability (e.g., 8 = -1, 10 = +0, 15 = +2).
    - Ensure total points used is less than or equal to 27.
    
  ### 4. Background Selection
    - The system will show all available backgrounds. You must type in one from the list.
    - Grant specific skill proficiencies (e.g., "History" and "Religion" for Acolyte).
    - Include background-specific features (e.g., "Shelter of the Faithful").

# Part 3: Rules/Logic for the Chosen System
## Sample input and output:

### 1. Selecting a race with a subrace
```
Enter your character's name: Legolas

Enter your ability scores. Rules:
1. You have 27 points to distribute using point-buy.
2. Scores must be between 8 and 15 (before racial bonuses).
Score costs - 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9
Enter Strength score (8-15): 8
Points left:  27
Enter Dexterity score (8-15): 14
Points left:  20
Enter Constitution score (8-15): 14
Points left:  13
Enter Intelligence score (8-15): 10
Points left:  11
Enter Wisdom score (8-15): 15
Points left:  2
Enter Charisma score (8-15): 10
Points left:  0
Available races: Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling
Choose a race: Elf
Available subraces: High Elf, Wood Elf, Drow
Choose a subrace: Wood Elf
Available classes: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
Choose a class: Ranger
Available backgrounds: Acolyte, Charlatan, Criminal, Entertainer
Choose a background: Charlatan

Character Creation Complete!
Name: Legolas
Race: Elf (Wood Elf)
Class: Ranger
Background: Charlatan
Ability Scores: {'Strength': 8, 'Dexterity': 16, 'Constitution': 14, 'Intelligence': 10, 'Wisdom': 16, 'Charisma': 10}
Modifiers: {'Strength': -1, 'Dexterity': 3, 'Constitution': 2, 'Intelligence': 0, 'Wisdom': 3, 'Charisma': 0}
Hit Points: 12
Proficiencies: Light armor, Medium armor, Shields, Simple weapons, Martial weapons, Deception, Sleight of Hand
Features: Darkvision, Keen Senses, Fey Ancestry, Trance, Favored Enemy, Natural Explorer, Fighting Style, Primeval Awareness, False Identity
```
### 2. Selecting a race without a subrace
```
Enter your character's name: Aragorn

Enter your ability scores. Rules:
1. You have 27 points to distribute using point-buy.
2. Scores must be between 8 and 15 (before racial bonuses).
Score costs - 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9
Enter Strength score (8-15): 12
Points left:  23
Enter Dexterity score (8-15): 14
Points left:  16
Enter Constitution score (8-15): 14
Points left:  9
Enter Intelligence score (8-15): 10
Points left:  7
Enter Wisdom score (8-15): 12
Points left:  3
Enter Charisma score (8-15): 11
Points left:  0
Available races: Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling
Choose a race: Human
Available classes: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
Choose a class: Fighter
Available backgrounds: Acolyte, Charlatan, Criminal, Entertainer
Choose a background: Acolyte

Character Creation Complete!
Name: Aragorn
Race: Human (Standard)
Class: Fighter
Background: Acolyte
Ability Scores: {'Strength': 13, 'Dexterity': 15, 'Constitution': 15, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 12}
Modifiers: {'Strength': 1, 'Dexterity': 2, 'Constitution': 2, 'Intelligence': 0, 'Wisdom': 1, 'Charisma': 1}
Hit Points: 12
Proficiencies: All armor, Shields, Simple weapons, Martial weapons, Insight, Religion
Features: , Fighting Style, Second Wind, Action Surge, Martial Archetype, Shelter of the Faithful
```
### 3. Going over the ability score limit
```
Enter your character's name: Shane

Enter your ability scores. Rules:
1. You have 27 points to distribute using point-buy.
2. Scores must be between 8 and 15 (before racial bonuses).
Score costs - 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9
Enter Strength score (8-15): 15
Points left:  18
Enter Dexterity score (8-15): 15
Points left:  9
Enter Constitution score (8-15): 15
Points left:  0
Enter Intelligence score (8-15): 15
Points left:  -9
Enter Wisdom score (8-15): 15
Points left:  -18
Enter Charisma score (8-15): 15
Points left:  -27
Error: Ability scores exceed allowed total!
```
# Part 4: Reflection
### Project Overview:
This project prompts the user to create a D&D character by asking for their name, ability scores 1 by 1, race, subrace (if applicable), class, and background. It uses logic to ensure that you don't go over the maximums or below the minimum scores when selecting ability scores. It also checks if any subraces apply to the selected race and displays only those options if so. Finally, it calculates your hit points and ability score modifiers based on the input ability scores and racial bonuses, then adds all proficiencies and features provided by your race, class, and background.

### Challenges:
**Order of Operations:**
  - When I first copied the code over from ChatGPT, it didn't work because a piece of the code for picking a class required abilitiy scores to already be in place. I had to move that piece of code in front for it to work properly

**Not Adding Racial Bonus:**
  - Initially, the code was calculating the modifiers before adding the bonus ability scores for the selected race, so that bonus didn't translate to the modifier.

**Inconsistencies When Editing:**
  - The sample code only gave me a couple classes, races and backhrounds, so I asked it to provide all options from the rules. However, when it did so, it changed the structure of the data so that it no longer worked with the rest of the code. This required me to ask chatGPT to rewrite some things as well as me manually editing some things when ChatGPT didn't understand what I asked for.

**ChatGPT Character Limit:**
  - ChatGPT can only produce so much code at once, so when I tried to get it to expand the backgrounds, it only got a few before it reached the character limit.
