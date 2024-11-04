import random

# 1. Game Setup: Define choices and initialize scores
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
# 2. Ascii art
rock_art = """
      _______
    ---'   ____)
          (_)
          (_)
          ()
    ---.(_)
"""

paper_art = """
       _______
    ---'    ___)___
              ______)
             _______)
            _______)
    ---.)
"""

scissors_art = """
       _______
    ---'   ___)___
              ______)
           __________)
          ()
    ---.(_)
"""


# 3. Instructions: Welcome message
print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to exit the game.")

# 4. Get number of rounds from the player (Best of X feature)
rounds = int(input("Enter the number of rounds to play (e.g., 3 for best of 3): "))

# 5. Game Flow: Loop to allow repeated rounds of play
while player_score < rounds and computer_score < rounds:
    user_action = input("Enter your choice (rock, paper, scissors): ").lower().strip()

    if user_action == "quit":
        print("Thanks for playing!")
        print(f"Final Scores - Player: {player_score}, Computer: {computer_score}")
        break
    elif user_action not in choices:
        print("Invalid choice, please enter 'rock', 'paper', or 'scissors'.")
        continue

    # 6. Randomize computer choice
    computer_action = random.choice(choices)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
   #  7. Print ASCII art for user and computer choices
    if user_action == "rock":
        print(rock_art)
    elif user_action == "paper":
        print(paper_art)
    elif user_action == "scissors":
        print(scissors_art)

    # 8. Determine the Winner
    if user_action == computer_action:
        result = "It's a tie!"
    elif (user_action == "rock" and computer_action == "scissors") or \
         (user_action == "scissors" and computer_action == "paper") or \
         (user_action == "paper" and computer_action == "rock"):
        result = "You win this round!"
        player_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    # 9. Print round summary
    print(f"Round Summary: You chose {user_action}, Computer chose {computer_action}. {result}")
    print(f"Current Scores - Player: {player_score}, Computer: {computer_score}")

# 10. Ending the Game: Final message
if player_score == rounds:
    print("Yay, you won!")
elif computer_score == rounds:
    print("Oh NO,computer won.")



