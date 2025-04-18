# Caesar Cipher Program 🔐

A simple Python program that performs encryption and decryption using the **Caesar Cipher** technique. This classic encryption method shifts characters in a message by a fixed number of positions in the alphabet.

## 🧠 How It Works

The Caesar Cipher works by shifting each letter in a message by a user-specified number (called the "shift"). For example, with a shift of 3:
- `A` becomes `D`
- `B` becomes `E`
- ...
- `Z` becomes `C`

This program:
- Encrypts and decrypts both uppercase and lowercase letters
- Ignores and retains non-alphabetic characters (spaces, punctuation, digits)
- Validates shift values between 0 and 25

## 📋 Features

- ✅ Encrypt a message
- ✅ Decrypt a message
- ✅ Input validation for shift value
- ✅ User-friendly menu system

## 🚀 Usage

Run the script using Python:

```bash
python caesar_cipher.py
```

You’ll be presented with a menu to choose between:
- Encryption
- Decryption
- Exit

## 📌 Example

```
=====================================
        Caesar Cipher Program        
=====================================
Select an option:
1 - Encrypt a message
2 - Decrypt a message
3 - Exit
-------------------------------------
Enter your choice (1, 2, or 3): 1
Enter the message to encrypt: Hello, World!
Enter the shift value (0-25): 3
Encrypted Message: Khoor, Zruog!
```

## 🛠 Functions

### `encrypt(message, shift)`
Encrypts the input `message` by shifting characters by the given `shift`.

### `decrypt(message, shift)`
Decrypts the input `message` using the reverse shift.

### `get_valid_shift()`
Prompts the user for a valid shift value between 0 and 25.

## 🧑‍💻 Author

Created as part of an educational project on basic cryptography techniques in Python.

## 📜 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
```
