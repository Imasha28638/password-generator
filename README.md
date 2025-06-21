# 🔐 Password Generator

A simple Python program that generates secure, customizable passwords with letters, numbers, and symbols.

## 📌 Features

- Choose how many **letters**, **numbers**, and **symbols** to include
- Randomly shuffles characters for added security
- Password strength indicator (weak / medium / strong)
- Optionally copy the password to your clipboard (requires `pyperclip`)

## 🧪 How It Works

1. The program asks the user for:
   - Number of letters
   - Number of numbers
   - Number of symbols
2. It generates a random password using Python's `random` and `string` modules.
3. The password is shuffled and displayed with a strength rating.

## 💻 Usage

Run the program using Python 3:


```bash
python password_generator.py
```

Example inputs

How many letters would you like in your password?
4
How many numbers would you like in your password?
3
How many symbols would you like in your password?
2


Example output

Your password is: a9#L6R@s
Password Length is 8 characters.
Password strength is medium !!!

Optional:

Install the pyperclip library if you want to copy passwords automatically:

```bash
pip install pyperclip
```

Pull requests are welcome! Feel free to open an issue if you have suggestions or bugs to report.
