from random import choice

options = ["Rock", "Paper", "Scissor"]
computer = choice(options)
player = input("Enter your choice (Rock, Paper, Scissor): ")

print(f"You chose {player}, Computer chose {computer}.")

# Check for tie
if player == computer:
    print("Looks like we're evenly matched.")
# Check for player win
elif (
    (player == "Rock" and computer == "Scissor") or
    (player == "Paper" and computer == "Rock") or
    (player == "Scissor" and computer == "Paper")
):
    print("You got lucky this time...")
# If not tie or player win, then the computer wins
else:
    print("Better luck next time!")
