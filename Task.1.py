
def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char >= 'a' and char <= 'z':
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            encrypted_message += new_char

        elif char >= 'A' and char <= 'Z':
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            encrypted_message += new_char

        else:
            encrypted_message += char

    return encrypted_message


def decrypt(message, shift):
    decrypted_message = ""

    for char in message:
        if char >= 'a' and char <= 'z':
            position = ord(char) - ord('a')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('a'))
            decrypted_message += new_char

        elif char >= 'A' and char <= 'Z':
            position = ord(char) - ord('A')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('A'))
            decrypted_message += new_char

        else:
            decrypted_message += char

    return decrypted_message


# Validate shift value
def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter the shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 0 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 0 and 25.")



while True:
    print("=====================================")
    print("        Caesar Cipher Program        ")
    print("=====================================")
    print("Select an option:")
    print("1 - Encrypt a message")
    print("2 - Decrypt a message")
    print("3 - Exit")
    print("-------------------------------------")

    option = input("Enter your choice (1, 2, or 3): ")

    if option == "1":
        text = input("Enter the message to encrypt: ")
        shift = get_valid_shift()
        encrypted_text = encrypt(text, shift)
        print("Encrypted Message:", encrypted_text)
        print()

    elif option == "2":
        text = input("Enter the message to decrypt: ")
        shift = get_valid_shift()
        decrypted_text = decrypt(text, shift)
        print("Decrypted Message:", decrypted_text)
        print()

    elif option == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please enter 1, 2, or 3.")
        print()

