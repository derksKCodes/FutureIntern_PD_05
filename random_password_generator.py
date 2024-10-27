import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    # Build the character set based on user's selection
    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_numbers:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation
    
    # Ensure the user has selected at least one character set
    if not character_set:
        return "Please select at least one character type."
    
    # Generate a random password using the chosen character set
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    try:
        # Get password length from the user
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        # Get character type preferences from the user
        use_uppercase = input("Include uppercase letters? (Y/N): ").lower() == "y"
        use_lowercase = input("Include lowercase letters? (Y/N): ").lower() == "y"
        use_numbers = input("Include numbers? (Y/N): ").lower() == "Y"
        use_special = input("Include special characters? (Y/N): ").lower() == "y"
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number for the password length.")

# Start the program
main()
