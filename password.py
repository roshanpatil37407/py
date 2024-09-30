import random
import string

def generate_password(length=8):
    # Define the characters that can be used in the password
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # Special characters (!, @, #, etc.)
    
    # Combine all the characters
    all_characters = letters + digits + symbols
    
    # Ensure at least one letter, digit, and symbol is in the password
    password = [
        random.choice(letters), 
        random.choice(digits), 
        random.choice(symbols)
    ]
    
    # Fill the remaining length of the password
    password += random.choices(all_characters, k=length-3)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert list to string and return the password
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    try:
        # Get the desired password length from the user
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Your generated password is: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
