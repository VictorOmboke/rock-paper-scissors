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

#function to handle when player wins a round
def player_round_win(player_choice, computer_choice):
    """Display information for when the player wins a round.

    Args:
        player_choice (str): the players choice of rock, paper, or scissors.
        computer_choice (str): the computers choice of rock, paper, or scissors.
    """
    print("** You win this round! **")
    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

def computer_round_win(player_choice, computer_choice):
    """Display information for when the computer wins a round.

    Args:
        player_choice (str): the players choice of rock, paper, or scissors.
        computer_choice (str): the computers choice of rock, paper, or scissors.
    """
    print("** The computer wins this round! **")
    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

#Function to ask the user if they want to play again
def play_again():
    """Prompt the user for a yes or no if they want to play again.

    """
    #Initialize accepted responses in a tuple.
    responses = ("yes", "no")
    prompt = True
    #Repeatedly prompt user if they want to keep playing or not.
    while prompt:
        user_input = input("Would you like to play again? (enter 'yes' or 'no') ").lower().strip()
        #Check if users input is one of the acceptable responses.
        if user_input not in responses:
            print("invalid input, please enter 'yes' or 'no'.")
        #Handle when user does want to play again.
        elif user_input in responses and user_input == "yes":
            prompt = False
            print("Great, have fun!")
            #Play the game again by calling main game function.
            play_game()
        #Handle when user does not want to play again.
        elif user_input in responses and user_input == "no":
            prompt = False
            print("Thanks for playing!")

##Create main game loop
def play_game():
    """Handle the flow of the game.
    """
    player_score = 0
    computer_score = 0
    #Main game loop will loop until user or computer score is 3.
    while player_score != 3 and computer_score != 3:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        #Winning conditions for the user
        if (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
            player_round_win(player_choice, computer_choice)
            player_score += 1
            print(f"current score: You - {player_score} | Computer - {computer_score}")
        #Winning conditions for the computer.
        elif (computer_choice == "rock" and player_choice == "scissors") or \
            (computer_choice == "paper" and player_choice == "rock") or \
            (computer_choice == "scissors" and player_choice == "paper"):
            computer_round_win(player_choice, computer_choice)
            computer_score += 1
            print(f"current score: You - {player_score} | Computer - {computer_score}")
        else:
            #Message to handle a tie.
            print("Its a tie!")
            print(f"Your choice: {player_choice}")
            print(f"Computer's choice: {computer_choice}")
    #Declare the winner and ask the user if they want to play again.
    if player_score == 3:
        print("Congrats you win!")
        play_again()
    elif computer_score == 3:
        print("The computer wins!")
        play_again()

play_game()