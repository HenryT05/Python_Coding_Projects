from cipher import encrypt, decrypt
from hashing import sha256_hash, integrity_check

def main():
    '''
    Prints out the CLI interface for the user
    and asks what the user wants to cipher or hash.
    returns:
        the choice and message that the user called for.
    '''
    while True:
        print("=== Crypto Tool ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Hash a message (SHA-256)")
        print("4. Check if two messages match by hash")
        print("5. Exit")

        choice = input("Choose(1-5): ")
        if choice == '1':
            message = input("What message to Encrypt?: ")
            shift = int(input("How much should message shift by?: "))
            print(encrypt(message, shift))
        elif choice == '2':
            message = input("What message to Decrypt?: ")
            shift = int(input("How much should message be decrypted by?: "))
            print(decrypt(message, shift))
        elif choice == '3':
            message = input("what message to Hash?: ")
            print(sha256_hash(message))
        elif choice == '4':
            message1 = input("What first message to check integrity?: ")
            message2 = input("whats the second message to compare?: ")
            print(integrity_check(message1, message2))
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again")


main()
