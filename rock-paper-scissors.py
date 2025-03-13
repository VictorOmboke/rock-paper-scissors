#Import random module
import random

#Display a welcome message and explain the rules of the game
print("Welcome to Rock, Paper, Scissors!")
print("Rules: You will be playing against a computer where you will pick rock, paper, or scissors and first to reach 3 wins will be crowned champion!")

##Get players choice
def get_player_choice():
    """Prompt user to enter rock, paper, or scissors.
    
    Return: player_choice - variable holding the players choice.
    """
    prompt = True
    #Initialize while loop to continually ask user to enter correct input.
    while prompt:
        player_choice = input("Please enter 'rock', 'paper', or 'scissors'. ").lower().strip()
        #Handle case where user enters anything that is not a letter.
        if player_choice.isalpha() == False:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        #Handle case where user enters letters but they are not the appropriate input.
        elif player_choice.isalpha() == True and player_choice not in ("rock", "paper", "scissors"):
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        #Handle case where user enters nothing.
        elif player_choice == "":
            print("No input detected. Please enter 'rock', 'paper', or 'scissors'.")
        else:
            prompt = False
            print(f"Your choice: {player_choice}!")
            return player_choice

##Generate computers choice
def get_computer_choice():
    """Generate a random choice of rock, paper, or scissors for the computer.

    Return: computer_choice - variable holding the computers choice.
    """
    #List with possible choices
    options = ["rock", "paper", "scissors"]
    #Choose a random element from the options list.
    computer_choice = random.choice(options)
    return computer_choice

#Determine the winner

#Track score

#Display results

#ask user to play again

##Create main game loop