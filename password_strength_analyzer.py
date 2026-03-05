def analyze_password(password: str) -> tuple[str, list[str]]:
    MIN_LENGTH = 8
    COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123"}
    has_length = len(password) >= MIN_LENGTH
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char.isspecial() for char in password)
    is_common = password in COMMON_PASSWORDS
    return "Unknown", ["Coming soon!"] 


def main():
    password = input("Enter a strong password: ")
    strength, feedback = analyze_password(password)
    print(f"It's a {strength} password")

if __name__ == "__main__":
    main()