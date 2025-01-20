from modules.character import Character
from modules.data import RACES, CLASSES, BACKGROUNDS
from modules.rules import Race, Class, Background, RuleEngine

def main():
    # Initialize character
    character = Character()

    # Input: Name
    character.name = input("Enter your character's name: ")

    # Input: Ability Scores
    print("\nEnter your ability scores. Rules:")
    print("1. You have 27 points to distribute using point-buy.")
    print("2. Scores must be between 8 and 15 (before racial bonuses).")
    print("Score costs - 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9")

    scores = {}
    for ability in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
        while True:
            try:
                score = int(input(f"Enter {ability} score (8-15): "))
                if score < 8 or score > 15:
                    raise ValueError("Scores must be between 8 and 15.")
                scores[ability] = score
                RuleEngine.display_points_left(scores)
                break
            except ValueError as e:
                print(e)

    try:
        RuleEngine.validate_ability_scores(scores)
    except ValueError as e:
        print(f"Error: {e}")
        return

    character.ability_scores.update(scores)
    
    # Input: Race
    print("Available races:", ", ".join(RACES.keys()))
    race = input("Choose a race: ")
    subrace = None
    if RACES[race].get("subraces"):
        print("Available subraces:", ", ".join(RACES[race]["subraces"]))
        subrace = input("Choose a subrace: ")
    Race.apply(character, race, subrace)
    character.calculate_modifiers()

    # Input: Class
    print("Available classes:", ", ".join(CLASSES.keys()))
    character_class = input("Choose a class: ")
    Class.apply(character, character_class)

    # Input: Background
    print("Available backgrounds:", ", ".join(BACKGROUNDS.keys()))
    background = input("Choose a background: ")
    Background.apply(character, background)

    # Output: Character Sheet
    print("\nCharacter Creation Complete!")
    print(f"Name: {character.name}")
    print(f"Race: {character.race} ({character.subrace})")
    print(f"Class: {character.character_class}")
    print(f"Background: {character.background}")
    print(f"Ability Scores: {character.ability_scores}")
    print(f"Modifiers: {character.modifiers}")
    print(f"Hit Points: {character.hit_points}")
    print(f"Proficiencies: {', '.join(character.proficiencies)}")
    print(f"Features: {', '.join(character.features)}")

if __name__ == "__main__":
    main()