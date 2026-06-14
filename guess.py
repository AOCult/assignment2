import random

# Generate a pseudorandom integer between 1 and 10, inclusive
secret_number = random.randint(1, 10)

# Ask the user for their single guess
guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess is correct and print the message
if guess == secret_number:
    print("Correct!")
else:
    print("Incorrect! The number was", secret_number)
