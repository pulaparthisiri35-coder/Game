import random
from collections import Counter

def play_game():
    options = ["rock", "paper", "scissors"]
    user_history = []
    scores = {"user": 0, "computer": 0}

    print("--- AI Rock-Paper-Scissors ---")
    print("The AI is learning your patterns. Type 'quit' to end.")

    while True:
        # AI Logic: Predict user's move based on most frequent past move
        if len(user_history) < 3:
            computer_choice = random.choice(options)
        else:
            # Predict user plays their most common move and pick the counter
            most_common_move = Counter(user_history).most_common(1)[0][0]
            if most_common_move == "rock": computer_choice = "paper"
            elif most_common_move == "paper": computer_choice = "scissors"
            else: computer_choice = "rock"

        user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

        if user_choice == "quit":
            break
        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue

        user_history.append(user_choice)
        print(f"AI chose: {computer_choice}")

        # Determine Winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            scores["user"] += 1
        else:
            print("AI wins this round!")
            scores["computer"] += 1

        print(f"Scoreboard -> You: {scores['user']} | AI: {scores['computer']}")

    print("\nFinal Game Over!")
    print(f"Final Score -> You: {scores['user']} | AI: {scores['computer']}")

if __name__ == "__main__":
    play_game()
  output:
--- AI Rock-Paper-Scissors ---
The AI is learning your patterns. Type 'quit' to end.

Enter Rock, Paper, or Scissors: rock
AI chose: scissors
You win this round!
Scoreboard -> You: 1 | AI: 0

Enter Rock, Paper, or Scissors: rock
AI chose: paper
AI wins this round!
Scoreboard -> You: 1 | AI: 1

Enter Rock, Paper, or Scissors: quit
Final Game Over!
Final Score -> You: 1 | AI: 1
