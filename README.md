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

### Chosen Idea: Character Creator for D&D 5e

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
    - Update character proficiencies.


# Part 3: Rules/Logic for the Chosen System
Sample input and output:

Enter your ingredients (comma-separated): chicken, rice, soy sauce You are close to making Chicken Fried Rice! Missing: garlic.

Enter your ingredients (comma-separated): garlic, soy sauce No recipes match. Try adding more ingredients.

Enter your ingredients (comma-separated): pasta, tomatoes, garlic, olive oil You can make Spaghetti Pomodoro!

# Part 4: Reflection
### Project Overview:
This project involved designing a practical, rule-based system to recommend recipes based on user inputs. The system uses logical conditions (e.g., exact and partial matches) to evaluate user-provided ingredients against recipes in the dataset.

### Challenges:
Handling Partial Matches:
Deciding on a threshold (75%) that balances flexibility with accuracy was challenging.
Common Ingredients:
Ensuring common ingredients like salt and water don’t skew the results. I resolved this by excluding them from the missing ingredient list.
