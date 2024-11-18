import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed = False

    # Game loop
    while not guessed:
        # Get the user's guess
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        # Check if the guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            guessed = True

# Start the game
guess_the_number()
