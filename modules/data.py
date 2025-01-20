# Static data for races, classes, etc.
RACES = {
    "Dwarf": {
        "subraces": ["Hill Dwarf", "Mountain Dwarf"],
        "bonuses": {
            "Hill Dwarf": {"Constitution": 2, "Wisdom": 1},
            "Mountain Dwarf": {"Constitution": 2, "Strength": 2},
        },
        "features": ["Darkvision", "Dwarven Resilience", "Stonecunning"],
    },
    "Elf": {
        "subraces": ["High Elf", "Wood Elf", "Drow"],
        "bonuses": {
            "High Elf": {"Dexterity": 2, "Intelligence": 1},
            "Wood Elf": {"Dexterity": 2, "Wisdom": 1},
            "Drow": {"Dexterity": 2, "Charisma": 1},
        },
        "features": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
    },
    "Halfling": {
        "subraces": ["Lightfoot", "Stout"],
        "bonuses": {
            "Lightfoot": {"Dexterity": 2, "Charisma": 1},
            "Stout": {"Dexterity": 2, "Constitution": 1},
        },
        "features": ["Lucky", "Brave", "Halfling Nimbleness"],
    },
    "Human": {
        "subraces": [],
        "bonuses": {"Standard": {"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1}},
        "features": [],
    },
    "Dragonborn": {
        "subraces": [],
        "bonuses": {"Standard": {"Strength": 2, "Charisma": 1}},
        "features": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
    },
    "Gnome": {
        "subraces": ["Forest Gnome", "Rock Gnome"],
        "bonuses": {
            "Forest Gnome": {"Intelligence": 2, "Dexterity": 1},
            "Rock Gnome": {"Intelligence": 2, "Constitution": 1},
        },
        "features": ["Darkvision", "Gnome Cunning"],
    },
    "Half-Elf": {
        "subraces": [],
        "bonuses": {"Standard": {"Charisma": 2, "Flex": ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom"]}},
        "features": ["Darkvision", "Fey Ancestry", "Skill Versatility"],
    },
    "Half-Orc": {
        "subraces": [],
        "bonuses": {"Standard": {"Strength": 2, "Constitution": 1}},
        "features": ["Darkvision", "Relentless Endurance", "Savage Attacks"],
    },
    "Tiefling": {
        "subraces": [],
        "bonuses": {"Standard": {"Charisma": 2, "Intelligence": 1}},
        "features": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
    },
}

CLASSES = {
    "Barbarian": {
        "hit_die": 12,
        "features": ["Rage", "Unarmored Defense", "Reckless Attack", "Danger Sense"],
        "proficiencies": ["Light armor", "Medium armor", "Shields", "Simple weapons", "Martial weapons"],
    },
    "Bard": {
        "hit_die": 8,
        "features": ["Bardic Inspiration", "Jack of All Trades", "Song of Rest", "Expertise"],
        "proficiencies": ["Light armor", "Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords", "Three musical instruments of your choice"],
    },
    "Cleric": {
        "hit_die": 8,
        "features": ["Spellcasting", "Divine Domain", "Channel Divinity", "Turn Undead"],
        "proficiencies": ["Light armor", "Medium armor", "Shields", "Simple weapons"],
    },
    "Druid": {
        "hit_die": 8,
        "features": ["Spellcasting", "Wild Shape", "Druid Circle", "Timeless Body"],
        "proficiencies": ["Light armor (non-metal)", "Medium armor (non-metal)", "Shields (non-metal)", "Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears", "Herbalism kit"],
    },
    "Fighter": {
        "hit_die": 10,
        "features": ["Fighting Style", "Second Wind", "Action Surge", "Martial Archetype"],
        "proficiencies": ["All armor", "Shields", "Simple weapons", "Martial weapons"],
    },
    "Monk": {
        "hit_die": 8,
        "features": ["Martial Arts", "Unarmored Defense", "Ki", "Deflect Missiles"],
        "proficiencies": ["Simple weapons", "Shortswords", "One type of artisan's tools or musical instrument"],
    },
    "Paladin": {
        "hit_die": 10,
        "features": ["Divine Sense", "Lay on Hands", "Fighting Style", "Divine Smite"],
        "proficiencies": ["All armor", "Shields", "Simple weapons", "Martial weapons"],
    },
    "Ranger": {
        "hit_die": 10,
        "features": ["Favored Enemy", "Natural Explorer", "Fighting Style", "Primeval Awareness"],
        "proficiencies": ["Light armor", "Medium armor", "Shields", "Simple weapons", "Martial weapons"],
    },
    "Rogue": {
        "hit_die": 8,
        "features": ["Sneak Attack", "Thieves' Cant", "Cunning Action", "Evasion"],
        "proficiencies": ["Light armor", "Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords", "Thieves' tools"],
    },
    "Sorcerer": {
        "hit_die": 6,
        "features": ["Spellcasting", "Sorcerous Origin", "Font of Magic", "Metamagic"],
        "proficiencies": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
    },
    "Warlock": {
        "hit_die": 8,
        "features": ["Otherworldly Patron", "Pact Magic", "Eldritch Invocations", "Pact Boon"],
        "proficiencies": ["Light armor", "Simple weapons"],
    },
    "Wizard": {
        "hit_die": 6,
        "features": ["Spellcasting", "Arcane Recovery", "Arcane Tradition", "Spell Mastery"],
        "proficiencies": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
    },
}

BACKGROUNDS = {
    "Acolyte": {
        "skills": ["Insight", "Religion"],
        "languages": 2,
        "equipment": ["Holy symbol", "Prayer book", "5 sticks of incense", "Vestments", "Common clothes", "15 gp"],
        "features": ["Shelter of the Faithful"],
    },
    "Charlatan": {
        "skills": ["Deception", "Sleight of Hand"],
        "tools": ["Disguise kit", "Forgery kit"],
        "equipment": ["Fine clothes", "Disguise kit", "Con tools", "15 gp"],
        "features": ["False Identity"],
    },
    "Criminal": {
        "skills": ["Deception", "Stealth"],
        "tools": ["Gaming set", "Thieves' tools"],
        "equipment": ["Crowbar", "Dark clothes", "Belt pouch", "15 gp"],
        "features": ["Criminal Contact"],
    },
    "Entertainer": {
        "skills": ["Acrobatics", "Performance"],
        "tools": ["Disguise kit", "Musical instrument"],
        "equipment": ["Musical instrument", "Favor from admirer", "Costume", "15 gp"],
        "features": ["By Popular Demand"],
    },
}