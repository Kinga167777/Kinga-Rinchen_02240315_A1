import random
import time

def get_user_choice():
    while True:
        user_choice = input("What do you pick? (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Oops! Please choose 'rock', 'paper', or 'scissors'. Try again!")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win this round!"
    else:
        return "You lose this round!"

def play_again():
    while True:
        play_again_input = input("Wanna play again? (y/n): ").lower()
        if play_again_input == 'y':
            return True
        elif play_again_input == 'n':
            return False
        else:
            print("Please type 'y' for yes or 'n' for no!")

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors! Get ready to make your choice")
    time.sleep(1)  

    while True:
        user_choice = get_user_choice()
        print(f"You chose: {user_choice}")
        
        print("choosing.......")
        time.sleep(1)  

        computer_choice = get_computer_choice()
        print(f"I chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if not play_again():
            print("Thanks for playing my game")
            break
        else:
            print("ONce moreee")

rock_paper_scissors()
