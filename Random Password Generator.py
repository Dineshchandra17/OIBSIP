import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length <= 0:
                print("Password length should be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    use_letters = input("Include letters? (yes/no): ").strip().lower() in ['yes', 'y']
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() in ['yes', 'y']
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() in ['yes', 'y']

    return length, use_letters, use_numbers, use_symbols

def main():
    print("Welcome to the Random Password Generator!")
    length, use_letters, use_numbers, use_symbols = get_user_input()
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()