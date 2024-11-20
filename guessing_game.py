import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Set number of attempts
    attempts = 0
    guessed_number = None

    # Game loop
    while guessed_number != number_to_guess:
        guessed_number = int(input("Enter your guess: "))
        attempts += 1
        
        if guessed_number < number_to_guess:
            print("Too low! Try again.")
        elif guessed_number > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()

