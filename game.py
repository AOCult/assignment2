import random

def main():
    secret_number = random.randint(1, 25)
    for i in range(5):
        try:
            guess = int(input("Guess a number between 1 and 25: "))
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Correct!")
                return
        except ValueError:
            print("Please enter a valid integer.")
    print("The correct answer was", secret_number)

if __name__ == "__main__":
    main()
