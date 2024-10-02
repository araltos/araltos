# import secrets
# import string

# def get_random_uppercase():
#     """Generate a random uppercase letter."""
#     return secrets.choice(string.ascii_uppercase)

# def get_random_lowercase():
#     """Generate a random lowercase letter."""
#     return secrets.choice(string.ascii_lowercase)

# def get_random_digit():
#     """Generate a random digit."""
#     return secrets.choice(string.digits)

# def get_random_punctuation():
#     """Generate a random punctuation character."""
#     return secrets.choice(string.punctuation)

# def generate_additional_characters(length):
#     """Generate additional random characters."""
#     characters = string.ascii_letters + string.digits + string.punctuation
#     additional_characters = ''.join(secrets.choice(characters) for _ in range(length))
#     return additional_characters

# def shuffle_characters(password):
#     """Shuffle the characters of the password."""
#     password_list = list(password)
#     secrets.SystemRandom().shuffle(password_list)
#     return ''.join(password_list)

# def generate_strong_password(length=16):
#     """Generate a strong random password."""
#     uppercase_letter = get_random_uppercase()
#     lowercase_letter = get_random_lowercase()
#     digit = get_random_digit()
#     punctuation = get_random_punctuation()

    
#     all_characters = uppercase_letter + lowercase_letter + digit + punctuation
#     all_characters += generate_additional_characters(length - len(all_characters))
#     strong_password = shuffle_characters(all_characters)
    
#     return strong_password


# if __name__ == "__main__":
#     password_length = int(input("Enter the length of the password: "))
#     generated_password = generate_strong_password(password_length)
#     print("Generated Password:", generated_password)


import csv
import secrets
import string

def get_random_uppercase():
    """Generate a random uppercase letter."""
    return secrets.choice(string.ascii_uppercase)

def get_random_lowercase():
    """Generate a random lowercase letter."""
    return secrets.choice(string.ascii_lowercase)

def get_random_digit():
    """Generate a random digit."""
    return secrets.choice(string.digits)

def get_random_punctuation():
    """Generate a random punctuation character."""
    return secrets.choice(string.punctuation)

def generate_additional_characters(length):
    """Generate additional random characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    additional_characters = ''.join(secrets.choice(characters) for _ in range(length))
    return additional_characters

def shuffle_characters(password):
    """Shuffle the characters of the password."""
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    return ''.join(password_list)

def generate_strong_password(length=16):
    """Generate a strong random password."""
    uppercase_letter = get_random_uppercase()
    lowercase_letter = get_random_lowercase()
    digit = get_random_digit()
    punctuation = get_random_punctuation()

    all_characters = uppercase_letter + lowercase_letter + digit + punctuation
    all_characters += generate_additional_characters(length - len(all_characters))
    strong_password = shuffle_characters(all_characters)
    
    return strong_password

def write_password_hint_to_csv(password, hint):
    """Write a password and its corresponding hint to the CSV file."""
    csv_file = "password_hints.csv"

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([password, hint])

    print(f"Password and its hint have been saved to {csv_file}")

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_strong_password(password_length)
    print("Generated Password:", generated_password)

    hint = input("Enter a hint for the password: ")
    write_password_hint_to_csv(generated_password, hint)
