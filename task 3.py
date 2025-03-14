import random
import string
import re

def generate_random_password():
    print("\n--- Secure Password Generator ---")
    
   
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
    except ValueError:
        print("Invalid input! Using default length of 8.")
        length = 8

    if length < 8:
        print("Password length too short! Setting length to 8.")
        length = 8

    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*"

    
    password_chars = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

   
    all_chars = uppercase_letters + lowercase_letters + digits + special_characters
    password_chars += random.choices(all_chars, k=length - 4)

    
    random.shuffle(password_chars)

    
    password = ''.join(password_chars)

    print(f"\nGenerated Password: {password}\n")
    return password


def check_password_strength():
    print("\n--- Password Strength Checker ---")
    
    
    password = input("Enter a password to check its strength: ")

   
    if len(password) < 8:
        strength = "Weak"
    elif re.fullmatch(r'[A-Za-z]+', password):
        strength = "Weak"
    elif re.fullmatch(r'\d+', password):
        strength = "Weak"
    elif (
        len(password) >= 8 and
        re.search(r'[A-Za-z]', password) and
        re.search(r'\d', password) and
        not re.search(r'[!@#$%^&*]', password)
    ):
        strength = "Medium"
    elif (
        len(password) >= 10 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*]', password)
    ):
        strength = "Strong"
    else:
        
        strength = "Medium"

    print(f"\nPassword Strength: {strength}\n")


def main():
    print("==== Python Password Project ====\n")
    
    
    generate_random_password()
    
    
    check_password_strength()

    print("==== End of Program ====")


if __name__ == "__main__":
    main()
