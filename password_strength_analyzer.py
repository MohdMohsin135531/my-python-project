def analyze_password(password: str) -> tuple[str, list[str]]:
    MIN_LENGTH = 8
    COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123"}
    SPECIAL_CHAR = set("!@#$%^&*()_+-=[]{}|;:,.<>?")
    has_length = len(password) >= MIN_LENGTH
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in SPECIAL_CHAR for char in password)
    is_common = password.lower() in COMMON_PASSWORDS
    if has_length and has_special and has_upper and has_lower and has_digit and not is_common:
        return "Strongest", ["You use a very strong password"]
    


def main():
    password = input("Enter a strong password: ")
    strength, feedback = analyze_password(password)
    print(f"Strength = {strength}")
    print(f"Feedback = {feedback}")

if __name__ == "__main__":
    main()