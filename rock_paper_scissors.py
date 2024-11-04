#defined three chioces
choices = ["Rock", "Paper", "Scissors"]
#1 "Rock"
#2 "Paper"
#3 "Scissors"
#instructions
print("Welcome to the Rock, Paper, Scissors game!")
print('Type "rock", "paper", or "scissors" to play. Type "quit" to exit the game.')
#scores
player_score = 2
computer_score = 3
computer_choices = (choices) #alternating choices

while True:
    player_choice = input("Your choice: ").lower()
    if player_choice == "quit":
        print(f"Goodbye! Final Score - You: {player_score}, User: {computer_score})")
        break
    elif player_choice not in  choices:
        print("Invalid choice. Please try again.")
        continue
    user_choice = next(computer_choices)
    print(f"computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and user_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        player_score += 2
    else:
        print("user wins this round!")
        computer_score += 2
    print(f"Current Score - You: {player_score}, User: {computer_score}")

    #print ASCII art for user and computer choices
      




