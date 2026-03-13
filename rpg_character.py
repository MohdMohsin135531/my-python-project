full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    
    if character_name == "":
        return "The character should have a name"

    if len(character_name) > 10:
        return "The character name is too long"

    if ' ' in character_name:
        return "The character name should not contain spaces"

    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return "All stats should be integers"
    
    if any(arg < 1 for arg in[strength, intelligence, charisma]):
        return "All stats should be no less than 1"

    if any(arg > 4 for arg in[strength, intelligence, charisma]):
        return "All stats should be no more than 4"

    if sum([strength, intelligence, charisma]) != 7:
        return "The character should start with 7 points"

    def stat_bar(value):
        return full_dot * value + empty_dot * (10 - value)

    return (
        f"{character_name}\n"
        f"STR {stat_bar(strength)}\n"
        f"INT {stat_bar(intelligence)}\n"
        f"CHA {stat_bar(charisma)}"
    )