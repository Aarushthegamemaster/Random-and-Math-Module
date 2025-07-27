import random

while True:
    user_action = str(input("Enter your choice(rock, paper or scissors):"))
    action_possible = ["Rock","Paper","Scissors"]
    action_ai = random.choice(action_possible)
    print(f"\nYou chose {user_action}, and the computer chose {action_ai}.\n")

    if user_action == action_ai:
        print(f"Both players selected {user_action}. It is a tie!")
    elif user_action == "Rock" or user_action == "rock":
        if action_ai == "scissors" or action_ai == "Scissors":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif user_action == "Paper" or user_action == "paper":
        if action_ai == "Rock" or action_ai == "rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "Scissors" or user_action == "scissors":
        if action_ai == "Paper" or action_ai == "paper":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")

    play_again = str(input("Do you want to play again? If yes type in y and if no type in n:"))
    if play_again != "y":
        print("Thank you for playing!")
        print("Please play again!")
        break
