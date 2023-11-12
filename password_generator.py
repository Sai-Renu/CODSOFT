import random
import string

def password_generator(length):
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation


    all_chars = lower_chars + upper_chars + digits + special_chars

    if length > len(all_chars):
        length = len(all_chars)

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

try:
    length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()


if length < 1:
    print("Password length should be at least 1.")
    exit()

password = password_generator(length)
print(f"Password generated: {password}")
