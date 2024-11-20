import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number I have in mind, between 1 and 100.")
    
    while True:
        # Step 1: Generate a random number
        target_number = random.randint(1, 100)
        attempts = 0
        print("\nI have picked a number. Let's start!")

        while True:
            try:
                # Step 2: Take player input
                player_guess = int(input("Enter your guess: "))
                attempts += 1

                # Step 3: Compare guesses
                if player_guess > target_number:
                    print("Too high, try again!")
                elif player_guess < target_number:
                    print("Too low, try again!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Step 4: Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    number_guessing_game()
