import pyfiglet 



def encrypt():
    text = input("Enter message to encrypt: ")
    shift =  int(input("Enter shift : "))
    text =  text.lower()
    enc = " "
    for char in text :
        if char.islower():
            enc += chr((ord(char) + shift -97) % 26 +97)
        else:
            enc += char
    print("Encrypted message is: ", enc )   
    
def decrypt():
    text = input("Enter message to decrypt: ")
    shift =  int(input("Enter shift : "))
    text = text.lower()
    dec = " "
    for char in text:
        if char.islower():
            dec += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            dec += char
    print("Decrypted message is: ", dec )
    
def main():
    print(pyfiglet.figlet_format("Caeser Cipher"))
    options = {
        "1": encrypt,
        "2": decrypt,
        "3": lambda: print("Exiting program. Goodbye!") or exit()
    }
    print("\nChoose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    
    action = options.get(choice)
    if action:
        action()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
