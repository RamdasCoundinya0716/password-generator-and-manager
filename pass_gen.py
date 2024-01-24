import random

password_config = {
    'letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    'numbers': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'symbols': ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?'],
}
def generate_password(no_of_letters, no_of_symbols, no_of_numbers):
    # Ensure a minimum of 8 characters
    total_characters = no_of_letters + no_of_symbols + no_of_numbers
    if total_characters < 8:
        return "Error: Minimum 8 characters required. Please adjust your choices."
    
    password = []
    password.extend(random.sample(password_config['letters'], no_of_letters))
    password.extend(random.sample(password_config['symbols'], no_of_symbols))
    password.extend(random.sample(password_config['numbers'], no_of_numbers))
    random.shuffle(password)
    final_password = ''.join(map(str, password))
    return final_password

# Get user input for the number of letters, symbols, and numbers
no_of_letters = random.randint (8, 10)
no_of_symbols = random.randint (2, 4)
no_of_numbers = random.randint (2, 4)
