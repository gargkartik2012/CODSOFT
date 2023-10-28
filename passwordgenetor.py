# A password generator application using python

# Import the random module
import random

# Define the characters for different levels of complexity
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{};:,./?"

# A loop to prompt the user to specify the desired length and complexity of the password
while True:
    # Ask the user to enter the length of the password
    length = int(input("Enter the length of the password (or 0 to quit): "))

    # Check if the user wants to quit
    if length == 0:
        print("Thank you for using the password generator.")
        break

    # Check if the user entered a valid length
    if length < 4:
        print("Invalid length. The password must be at least 4 characters long.")
        continue

    # Ask the user to choose the complexity of the password
    print("Choose the complexity of the password:")
    print("1. Lowercase letters/words only")
    print("2. Lowercase and uppercase letters")
    print("3. Lowercase, uppercase, and digits")
    print("4. Lowercase, uppercase, digits, and symbols")
    complexity = int(input("Enter your choice: "))

    # Check if the user entered a valid complexity
    if complexity < 1 or complexity > 4:
        print("Invalid choice. Please try again.")
        continue

    # Generate the password using a combination of random characters
    password = ""
    for i in range(length):
        # Choose a random character based on the complexity level
        if complexity == 1:
            char = random.choice(lowercase)
        elif complexity == 2:
            char = random.choice(lowercase + uppercase)
        elif complexity == 3:
            char = random.choice(lowercase + uppercase + digits)
        else:
            char = random.choice(lowercase + uppercase + digits + symbols)
        # Append the character to the password
        password += char

    # Display the password
    print(f"The generated password is: {password}")
