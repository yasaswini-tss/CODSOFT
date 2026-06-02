import random

user_score = 0
computer_score = 0

while True:
    print("\n===== ROCK PAPER SCISSORS =====")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nPlay Again? (y/n): ").lower()

    if play_again != "y":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thank you for playing!")
        break