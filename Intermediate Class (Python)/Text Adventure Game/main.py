PlayAgain = True
def PlayAgainPrompt():
  global PlayAgain
  if input("Play Again? (Y/N)\n") != "Y":
    PlayAgain = False
  else:
    print("\n")
while PlayAgain == True:
  print("You are in an empty room. There are 3 exits, a white door(A), a black door(B), and a skylight(C)")
  print("\n") # Prints a new (blank) line
  mainRoom = input("Choose an exit: ")
  if mainRoom == "A":
    print("You have fallen in an endless pit.")
  elif mainRoom == "B":
    print("You entered an elevator which closes behind you. You are trapped in a constant upward motion")
  elif mainRoom == "C":
    print("You have stepped onto an escalator which goes on forever, bringing you closer and closer to the moon")
  else:
    print("You didn't put in A, B, or C")
    
  print("\n")
  PlayAgainPrompt()