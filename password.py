import random
import string

def check_password_strength(password):
    """Evaluates basic strength of the password based on simple criteria."""
    length_ok = len(password) >= 12
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

def generate_password(length=14):
    """Generates a random password containing letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== PassGuard: CLI Password Tool ===")
    print("1. Generate a strong random password")
    print("2. Check the strength of your password")
    
    choice = input("\nChoose an option (1 or 2): ").strip()

    if choice == "1":
        try:
            length = int(input("Enter password length (minimum 8, default 14): ") or 14)
            if length < 4:
                print("Password length too short! Setting length to 8.")
                length = 8
            new_password = generate_password(length)
            strength = check_password_strength(new_password)
            print(f"\nGenerated Password: {new_password}")
            print(f"Strength Rating:    {strength}")
        except ValueError:
            print("Invalid number format. Using default length 14.")
            new_password = generate_password(14)
            print(f"\nGenerated Password: {new_password}")

    elif choice == "2":
        user_pass = input("Enter password to evaluate: ")
        strength = check_password_strength(user_pass)
        print(f"\nPassword Strength: {strength}")

    else:
        print("Invalid selection. Exiting tool.")

if __name__ == "__main__":
    main()