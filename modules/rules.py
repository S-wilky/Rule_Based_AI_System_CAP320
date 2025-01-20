from modules.data import RACES, CLASSES, BACKGROUNDS

class Race:
    @staticmethod
    def apply(character, race_name, subrace=None):
        race_data = RACES[race_name]
        character.race = race_name
        if subrace:
            character.subrace = subrace
        else:
            character.subrace = "Standard"
            subrace = "Standard"
        for ability, bonus in race_data["bonuses"][subrace].items():
            character.ability_scores[ability] += bonus
        character.add_trait(", ".join(race_data["features"]))

class Class:
    @staticmethod
    def apply(character, class_name):
        class_data = CLASSES[class_name]
        character.character_class = class_name
        character.hit_points = class_data["hit_die"] + character.modifiers["Constitution"]
        character.proficiencies.extend(class_data["proficiencies"])
        character.features.extend(class_data["features"])

class Background:
    @staticmethod
    def apply(character, background_name):
        background_data = BACKGROUNDS[background_name]
        character.background = background_name
        character.proficiencies.extend(background_data["skills"])
        character.features.extend(background_data["features"])

class RuleEngine:
    @staticmethod
    def validate_ability_scores(scores):
        """Ensure ability scores follow D&D 5e rules."""
        point_costs = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
        total_points = 0
        for score in scores.values():
            total_points += point_costs.get(score, 0)
        if total_points > 27:  # Example for point-buy limits
            raise ValueError("Ability scores exceed allowed total!")
        for score in scores.values():
            if score < 8 or score > 15:
                raise ValueError("Scores must be between 8 and 15 (before racial bonuses).")
    
    @staticmethod
    def display_points_left(scores):
        point_costs = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
        total_points = 0
        for score in scores.values():
            total_points += point_costs.get(score, 0)
        points_left = 27 - total_points
        print("Points left: ", points_left)
