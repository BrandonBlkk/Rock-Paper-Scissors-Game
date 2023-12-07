import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if not player_choice in ("rock", "paper", "Scissors"):
        print("Invalid input!")
        quit()
    else:
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        choices = {"Player": player_choice,"Computer": computer_choice}
        return choices

def check_win(Player, Computer):
    print(f"You chose {Player} and computer chose {Computer}.")
    if Player == Computer:
        return "It's a tie!"
    elif Player == "rock":
        if Computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose"
    elif Player =="paper":
        if Computer == "rock":
            return "Paper covers rock! You win!" 
        else:
            return "Scissors cuts paper! You lose"
    elif Player == "scissors":
        if Computer == "paper":
            return "Scissors cuts paper! You win!"  
        else:
            return "Rock smashes scissors! You lose"

choices = get_choices()
result = check_win(choices["Player"], choices["Computer"])
print(result)


