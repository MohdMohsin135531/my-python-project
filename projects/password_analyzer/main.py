MIN_LENGTH = 8
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123"}
SPECIAL_CHAR = set("!@#$%^&*()_+-=[]{}|;:,.<>?")

def analyze_password(password: str) -> tuple[str, list[str]]:
    has_length = len(password) >= MIN_LENGTH
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in SPECIAL_CHAR for char in password)
    is_common = password.lower() in COMMON_PASSWORDS
    checks = [has_length, has_upper, has_lower, has_digit, has_special, not is_common]
    rule = sum(checks)
    feedback = ["At least 8 characters✅" if has_length else "Not 8 characters❌", 
                "Upper case✅" if has_upper else "No Upper case❌", 
                "Lower case✅" if has_lower else "No Lower case❌", 
                "Digits✅" if has_digit else "No Digits❌", 
                "Special character✅" if has_special else "No Special character❌", 
                "Not common✅" if not is_common else "Common❌"]
    if rule == 6:
        return "Strongest🔒", feedback
    elif rule >= 3:
        return "Moderate🔑", feedback
    else:
        return "Weak🔓", feedback
    


def main(): 
    password = input("Enter a strong password: ")
    strength, feedback = analyze_password(password)
    print(f"Strength = {strength}") 
    print("Feedback:")
    for hint in feedback:
        print(f"{hint}")

if __name__ == "__main__":
    main()