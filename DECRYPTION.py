def encrypt(text, shift):
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + shift)
    return encrypted
def decrypt(text, shift):
    decrypted = ""

    for char in text:
        decrypted += chr(ord(char) - shift)
    return decrypted

choice = input("Enter E to encrypt or D to decrypt: ").upper()
filename = input("Enter filename: ")
shift = 3
if choice == "E":
    with open(filename, "r") as file:
        content = file.read()
    encrypted_text = encrypt(content, shift)

    with open("encrypted.txt", "w") as file:
        file.write(encrypted_text)

    print("File encrypted successfully!")
    print("Saved as encrypted.txt")

elif choice == "D":
    with open(filename, "r") as file:
        content = file.read()

    decrypted_text = decrypt(content, shift)

    with open("decrypted.txt", "w") as file:
        file.write(decrypted_text)

    print("File decrypted successfully!")
    print("Saved as decrypted.txt")

else:
    print("Invalid choice.")