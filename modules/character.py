class Character:
    def __init__(self):
        self.name = ""
        self.race = None
        self.subrace = None
        self.character_class = None
        self.background = None
        self.alignment = None
        self.level = 1
        self.ability_scores = {"Strength": 10, "Dexterity": 10, "Constitution": 10,
                               "Intelligence": 10, "Wisdom": 10, "Charisma": 10}
        self.modifiers = None
        self.proficiencies = []
        self.features = []
        self.inventory = []
        self.hit_points = 0

    def calculate_modifiers(self):
        """Calculate ability score modifiers."""
        self.modifiers = {k: (v - 10) // 2 for k, v in self.ability_scores.items()}

    def add_trait(self, trait):
        if trait not in self.features:
            self.features.append(trait)