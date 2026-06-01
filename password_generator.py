import random
import string

while True:

    print("\n" + "=" * 40)
    print("      PASSWORD GENERATOR")
    print("=" * 40)

    length = int(input("Enter password length: "))

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    again = input("\nGenerate another password? (y/n): ")

    if again.lower() != "y":
        print("Thank you for using Password Generator!")
        break