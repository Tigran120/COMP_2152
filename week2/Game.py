from random import random

game=["Rock","Paper","Scissor"]
computer=random.choice(game)
x = input('Enter your choice: Rock, Paper, Scissor:')
if x=='Rock' and computer=='Rock':
    print("It's a tie!");
elif x=='Rock' and computer=='Paper':
    print("Computer wins!");
elif x=='Rock' and computer=='Scissor':
    print("Player wins!");
elif x=='Paper' and computer=='Paper':
    print("It's a tie!");
elif x=='Paper' and computer=='Scissor':
    print("Computer wins!");
elif x=='Scissor' and computer=='Scissor':
    print("It's a tie!");
elif x=='Scissor' and computer=='Rock':
    print("Computer wins!");
elif x=='Scissor' and computer=='Paper':
    print("Player wins!");
elif x=='Scissor' and computer=='Scissor':
