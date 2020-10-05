from random import randint

t = ['Rock', 'Paper','Scissors']

computer = t[randint(0,2)]
count = 0

player = False

while player == False :
    player = input("Player = Rock, Paper, or Scissors: ")
    print("Computer = Rock, Paper, or Scissors:",computer)
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("Player wins!")
        elif computer == "Scissors":
            print("Player wins!")
    elif player == "Paper":
        if computer == "Rock":
            print("Computer wins!")
        elif computer == "Scissors":
            print("Computer wins! Player looses!")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer wins!")
        elif computer == "Paper":
            print("Player wins!")
    else:
        print("Incorrect Spelling")
    player = False
    computer = t[randint(0, 2)]
