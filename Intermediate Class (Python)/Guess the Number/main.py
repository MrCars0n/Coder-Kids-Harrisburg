print("Think of a number in your head from 1-100 but don't tell me\n")

# Sets the range to select a number
max = 100
min = 0

# Creates answer variable
answer = ""

# Continues until the computer has not guessed your number
while answer != "equal":
  
  # Sets your number to half way betweeen your maximum and minimum number
  number = int((max + min) / 2)
  
  # The question of higher, lower, or equal
  answer = input("Is your number higher, lower, or equal to " + str(number) + "?")
  
  # Checking if the number shown was higher
  if answer == "higher":
    
    # Sets the number shwon to the miminum possible option
    min = number
    
  # Checking if the number shown was lower
  elif answer == "lower":
    
    # Sets the number shown to the maximum possible option
    max = number
    
  # Checking if the computer guesses the number
  elif answer == "equal":
    print("I won! Your number is " + str(number))
    
