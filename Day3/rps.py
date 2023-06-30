import random

choices = ["rock", "paper", "scissors"]
score = {"user": 0, "computer": 0, "draw": 0}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    while True:
        user_input = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

        if user_input == "q":
            break

        if user_input not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        winner = determine_winner(user_input, computer_choice)

        print(f"\nYou chose: {user_input}")
        print(f"The computer chose: {computer_choice}\n")

        if winner == "draw":
            score["draw"] += 1
            print("It's a draw!")
        elif winner == "user":
            score["user"] += 1
            print("You win!")
        else:
            score["computer"] += 1
            print("Computer wins!")

        print(f"\nScore - User: {score['user']}, Computer: {score['computer']}, Draws: {score['draw']}\n")

play_game()


