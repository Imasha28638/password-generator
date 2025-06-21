import random
import string
import pyperclip
# pyperclip is used to copy the generated password to the clipboard

def generate_password(n_letters, n_numbers, n_symbols):
    letters = string.ascii_letters  # Includes both lowercase and uppercase letters
    numbers = string.digits  # Includes digits from 0 to 9
    symbols = string.punctuation  # Includes common punctuation symbols

    password_list = []

    password_list += random.choices(letters, k=n_letters)
    password_list += random.choices(numbers, k=n_numbers)
    password_list += random.choices(symbols, k=n_symbols)
    # k= specifies the number of elements to choose

    random.shuffle(password_list)  # Shuffle the list to mix letters, numbers, and symbols

    return ''.join(password_list)  # Join the list into a single string

print("Welcome to the Password Generator!")

nLetters = int(input("How many letters would you like in your password?\n"))
nNumbers = int(input("How many numbers would you like in your password?\n"))
nSymbols = int(input("How many symbols would you like in your password?\n"))

if nLetters < 0 or nNumbers < 0 or nSymbols < 0 or nLetters > 25 or nNumbers > 25 or nSymbols > 25:
    print("Please enter non-negative values or less than 25 for letters, numbers, and symbols.")
    exit()

length = nLetters + nNumbers + nSymbols
password = generate_password(nLetters, nNumbers, nSymbols)

if nLetters + nNumbers + nSymbols < 8:
    strength = "❌  weak"
elif nLetters + nNumbers + nSymbols < 12:
    strength = "⚠️  medium"
else:
    strength = "✅  strong"

print(f"Your password is: {password}")
print(f"Password length is {length} characters.")
print(f"Password strength is {strength} !!!")

pyperclip.copy(password)  # Copy the generated password to the clipboard
print("Your password has been copied to the clipboard.")