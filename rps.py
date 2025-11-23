#importing random module
import random

choices = ["rock", "paper", "scissors"]
#user input 
while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice.")
        continue

    comp = random.choice(choices)
    print("Computer chose:", comp)
#game logic 
    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("You lose!")

    if input("Play again? (yes/no): ").lower() != "y":
        break
