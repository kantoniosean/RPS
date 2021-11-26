import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter Rock, Paper, or Scissors OR 'Quit' to quit: ").lower()
    if user_choice == "quit":
        break

    if user_choice not in options:
        print("Entry not valid")
        continue

    random_num = random.randint(0, 2)

    computer_choice = options[random_num]
    print("Computer chose " + str(computer_choice) + ".")

    if user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win")
        user_wins += 1

    elif user_choice == computer_choice:
        print("Tie. Try again")

    else:
        print("You lost :(")
        computer_wins += 1

    if computer_wins == 2 or user_wins == 2:
        if user_wins > computer_wins:
            print("You win the game!")
        else:
            print("You lost the game. Computer wins :(")
        break
