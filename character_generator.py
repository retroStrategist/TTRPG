#
# This program automatically builds a D&D 5e character with a race, class, and background
# Character features such as proficiency and expertise may be added over time
# This will never generate any character higher than level 1
# At that point you need to make your own decisions
# ChatGPT 3.5 was used to help build this program
#

import random

class Character:
    
    # Initializing function
    # ADD background, parameter
    # ADD self.character_background = background
    def __init__(self, character_class, background, val):
        self.character_class = character_class
        self.stats = self.generate_character_stats(val)
        self.modifiers = self.calculate_modifiers()
        self.character_background = background
        self.skills = self.generate_background_skills()
    
    def generate_background_skills(self):
        skills = set()
        background_skills_list = background_skills.get(self.character_background, [])
        for skill in background_skills_list:
            skills.add(skill)
        return skills
    
    def generate_class_skills(self):
        # Set of class skills available for the clas
        class_skill_set = set(class_skills.get(self.character_class))
        # Set of skills available for the background
        background_skill_set = set(background_skills.get(self.character_background))
        # Finds number of skills to add
        num_skills_to_add = class_skill_number.get(self.character_class)
        #Creates set of available skills from skills not already taken in the background
        available_skills = set((class_skill_set).difference(background_skill_set))
        # Adds proper number of skills
        for _ in range(num_skills_to_add):
            if available_skills:
                skill = available_skills.pop()
                self.skills.add(skill)
            else:
                break  
        return self.skills
        
    def generate_character_stats(self, val):
        priority_list = self.priority_stats.get(self.character_class)
        stats = {
            "Str" : 0,
            "Dex" : 0,
            "Con" : 0,
            "Int" : 0,
            "Wis" : 0,
            "Cha" : 0
        }
        
        if val == 1:
            rolled_stats = []
            for stat in priority_list:
                score = sorted([random.randint(1, 6) for _ in range(4)])# Rolls 4d6
                total_score = sum(score[1:]) # Drops the lowest
                rolled_stats.append(total_score) # Puts the score into the list of rolled stats 
                
            rolled_stats.sort(reverse = True) #sorts the list in descending order (Largest to smallest)
            print(rolled_stats)
            print(self.priority_stats.get(self.character_class))
            
            # Iterates through the rolled stats and priority list together
            for stat, score in zip(priority_list, rolled_stats): # Most important stat is first in priority_list
                stats[stat] = score # Assigns to stats in descending order
                
        # Accidental Roll Through method?
        # for stat in priority_list:
            # score = sum(sorted([random.randint(1, 6) for _ in range (4)])[1:]) # Rolls 4d6, drops lowest
             # stats[stat] = score
                
        if val == 2: # Standard Array
            score = [15, 14, 13, 12, 10, 8]
            print(self.priority_stats.get(self.character_class))
            for stat, value in zip(priority_list, score):
                stats[stat] = value
           
        return stats
    
    def calculate_racial_bonus(self, race, racial_bonus):
        if race in racial_bonus:
            bonus_list = racial_bonus[race]
        for stat, bonus in zip(self.stats.keys(), bonus_list):
            self.stats[stat] += bonus
            
    def print_stats(self):
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")
    
    def calculate_modifiers(self):
        modifiers = [(score - 10) // 2 for score in self.stats.values()]
        return modifiers
    
    def print_mods(self):
        for stat, value in self.stats.items():
            mod = (value - 10) // 2
            print(stat + ": " + str(mod))
        
    def print_skills(self):
        print("Your character has proficiency in")
        for skill in self.skills:
           print(skill)
            


 # Most important stats for each class
    priority_stats = {
        "Artificer" : ["Int", "Con", "Dex", "Str", "Cha", "Wis"],
        "Barbarian" : ["Str", "Con", "Dex", "Wis", "Int", "Cha"],
        "Bard" :  ["Cha", "Dex", "Con", "Str", "Wis", "Int"],
        "Cleric" :  ["Wis", "Con", "Str", "Dex", "Int", "Cha"],
        "Druid" : ["Wis", "Con", "Dex", "Str", "Int", "Cha"],
        "Fighter" : ["Str'", "Con", "Dex", "Wis", "Cha", "Int"],
        "Monk" : ["Wis", "Dex", "Con", "Str", "Int", "Cha"],
        "Paladin" : ["Str", "Cha", "Con", "Dex", "Wis", "Int"],
        "Ranger" : ["Dex", "Con", "Wis", "Str", "Int", "Cha"],
        "Rogue" : ["Dex", "Con", "Cha", "Wis", "Int", "Str"],
        "Sorcerer" : ["Cha", "Con", "Dex", "Wis", "Int", "Str"],
        "Warlock" : ["Cha", "Con", "Dex", "Wis", "Int", "Str"],
        "Wizard" : ["Int", "Con", "Wis", "Cha", "Dex", "Str"]
        }
    
# Saving throw Proficiency based on class
saving_throws = {
    "Artificer" : ["Con", "Int"],
    "Barbarian" : ["Str", "Con"],
    "Bard" : ["Dex", "Cha"],
    "Cleric" : ["Wis", "Cha"],
    "Druid" : ["Int", "Wis"],
    "Fighter" : ["Str", "Con"],
    "Monk" : ["Str", "Dex"],
    "Paladin" : ["Wis", "Cha"],
    "Ranger" : ["Str", "Dex"],
    "Rogue" : ["Dex", "Int"],
    "Sorcerer" : ["Con", "Cha"],
    "Warlock" : ["Wis", "Cha"],
    "Wizard" : ["Int", "Wis"]
}

# Stat bonuses based on race
# Uses list of numbers, which are added to corresponding stat
# [Str, Dex, Con, Int, Wis, Cha] in that order
racial_bonus = {
    "Dragonborn" : [2, 0, 0, 0, 0, 1], 
    "Dwarf": [0, 0, 2, 0, 0, 0],
    "Elf" : [0, 2, 0, 0, 0, 0],
    "Gnome" : [0, 0, 0, 2, 0, 0],
    "Half-Elf": [0, 0, 0, 0, 0, 2],
    "Halfling" : [0, 2, 0, 0, 0, 0],
    "Half-Orc" : [2, 0, 1, 0, 0, 0],
    "Human" : [1, 1, 1, 1, 1, 1],
    "Tiefling" : [0, 0, 0, 1, 0, 2]
}

# Skill proficiencies for class
#Define contastants for 
class_skills = {
    "Artificer" : ["Arcana", "History", "Investigation", "Medicine", "Nature", "Perception", "Sleight of Hand"],
    "Barbarian" : ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
    "Bard" : ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana", "Historty", "Investigation", "Nature", "Religion", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"],
    "Cleric" : ["History", "Insight", "Medicine", "Persuasion", "Religion"],
    "Druid" : ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
    "Fighter" : ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "Monk" : ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
    "Paladin" : ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
    "Ranger" : ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
    "Rogue" : ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
    "Sorcerer" : ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
    "Warlock" : ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
    "Wizard" : ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
    
}
#Number of skills each class gets at level 1
class_skill_number = {
    "Artificer" : 2,
    "Barbarian" : 2,
    "Bard" : 3,
    "Cleric" : 2,
    "Druid" : 2,
    "Fighter" : 2,
    "Monk" : 2,
    "Paladin" : 2,
    "Ranger" : 3,
    "Rogue" : 4,
    "Sorcerer" : 2,
    "Warlock" : 2,
    "Wizard" : 3
}
# Skill proficiencies for background
background_skills = {
    "Acolyte" : ["Insight", "Religion"],
    "Charlatan" : ["Deception", "Slieght of Hand"],
    "Criminal" : ["Deception", "Stealth"],
    "Entertainer" : ["Acrobatics", "Performance"],
    "Folk Hero" : ["Animal Handling", "Survival"],
    "Gladiator" : ["Actrobatics", "Performance"],
    "Guild Artisan" : ["Insight", "Persuasion"],
    "Hermit" : ["Medicine", "Religion"],
    "Noble" : ["History", "Persuasion"],
    "Outlander" : ["Athletics", "Survival"],
    "Sage" : ["Arcana", "History"],
    "Sailor" : ["Athletics", "Perception"],
    "Soldier" : ["Athletics", "Intimidation"],
    "Urchin" : ["Sleight of Hand", "Stealth"]
}

# List of classes
classes = [
    "Artificer",
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

# List of races
races = [
    "Dragonborn", 
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    "Human",
    "Tiefling" 
]

# List of backgrounds
backgrounds = [
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Entertainer",
    "Folk Hero",
    "Gladiator",
    "Guild Artisan",
    "Hermit",
    "Noble",
    "Outlander",
    "Sage",
    "Sailor",
    "Soldier",
    "Urchin"
]

def generate_character_race():
    return random.choice(races)
    
def generate_character_background():
    return random.choice(backgrounds)

def generate_character_class():
    return random.choice(classes)


# FIXME: Add additional features


val = int(input("Welcome to Audrey's D&D Character Generator! Would you like to use Rolled Stats (1), or Array (2)?: "))

char_race = generate_character_race()
char_background = generate_character_background()
char_class = generate_character_class()
player_character = Character(char_class, char_background, val)
player_character.calculate_racial_bonus(char_race, racial_bonus)
player_character.calculate_modifiers()
player_character.generate_class_skills()
print(f"Your character is a {char_race} {char_class} with the {char_background} background with the following stats:")
player_character.print_stats()
print("Their ability score modifiers are:")
player_character.print_mods()
player_character.print_skills()
