def encrypt(message, shift):
    encrypted = ""

    for char in message:
        if char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            encrypted += new_char

        elif char.islower():
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            encrypted += new_char

        else:
            encrypted += char

    return encrypted


def decrypt(message, shift):
    decrypted = ""

    for char in message:
        if char.isupper():
            position = ord(char) - ord('A')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('A'))
            decrypted += new_char

        elif char.islower():
            position = ord(char) - ord('a')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('a'))
            decrypted += new_char

        else:
            decrypted += char

    return decrypted


while True:
    print("\n===== CAESAR CIPHER =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))

        result = encrypt(message, shift)
        print("Encrypted message:", result)

    elif choice == "2":
        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))

        result = decrypt(message, shift)
        print("Decrypted message:", result)

    elif choice == "3":
        print("Thank you for using Caesar Cipher!")
        break

    else:
        print("Invalid choice. Please try again.")
