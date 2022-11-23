from random import *

RPS = ["R", "P", "S"]
playAgain = True
while playAgain == True:
  choice = input("Rock (R), Paper (P), or Scissors (S): ")
  compChoice = RPS[int(random()*3)]
  
  # Computer and You Tie
  if compChoice == choice:
    print("It is a tie!")
  
  # Computer Chose Rock
  elif compChoice == "R":
    # You chose Scissors
    if choice == "S":
      print("The computer chose Rock, you lost!")
    # You chose Paper
    elif choice == "P":
      print("The computer chose Rock, you won!")
      
  # Computer Chose Paper
  elif compChoice == "P":
    # Computer Chose Rock
    if choice == "R":
      print("The computer chose Paper, you lost!")
    # You Chose Scissors
    elif choice == "S":
      print("The computer chose Paper, you won!")
    
  # Computer Chose Scissors
  elif compChoice == "S":
    # Computer Chose Paper
    if choice == "P":
      print("The computer chose Scissors, you lost!")
    elif compChoice == "R":
      print("The computer chose Paper, you won!")
      
  # Choice to Play Again
  replayChoice = input("Play Again? (Y/N)")
  if replayChoice != "Y":
    playAgain = False
