import random

def game(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("Rock, Paper, Scissors Game")
        print("Choose: 1. Rock, 2. Paper, 3. Scissors, or 4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ")

        if user_choice == '4':
            break

        if user_choice not in ('1', '2', '3'):
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue

        user_choice = int(user_choice)
        choices = ['rock', 'paper', 'scissors']
        user_choice -= 1
        user_choice = choices[user_choice]

        computer_choice = random.choice(choices)

        print(f"Your choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        result = game(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")
    if (user_score>computer_score):
        print("You won")
    elif (user_score==computer_score):
        print("Its a tie")
    else:
        print("Computer won")
    print("Thanks for playing!")

play_game()
