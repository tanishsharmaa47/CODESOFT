import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    user_length = int(input("Enter the desired password length: "))
    if user_length <= 0:
        print("Password length must be greater than 0.")
    else:
        generated_password = generate_password(user_length)
        print(f"Your generated password is: {generated_password}")
except ValueError:
    print("Please enter a valid number.")
