import random

def guess_number_game():
    """
    A game where the player guesses a number randomly selected by the computer
    within a defined range. The user is continuously prompted for guesses until
    the correct number is guessed.
    
    Input: User guesses (integer).
    Output: Feedback on whether the guess is too low, too high, or correct.
    """
    print("\n--- Guess the Number Game ---")
    
   
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    attempts = 0
    while True:
        try:
        
            user_guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")

           
            if user_guess.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break

            user_guess = int(user_guess)

           
            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue

           
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.")
