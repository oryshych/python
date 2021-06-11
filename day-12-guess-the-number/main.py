#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

## Ver_1

# import random
# from art import logo

# guess_number = random.randint(1, 100)

# print (logo)
# print ("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100")
# #correct answer
# print(f"Pssst. The correct answer is {guess_number}")

# dif_level = input ("Choose a difficalty. Type 'easy' or 'hard': ").lower()
# level = 0
# if dif_level == "easy":
#   level = 10
# elif dif_level == "hard":
#   level = 5

# def game():
#   life = level
#   end_game = False
#   while not end_game:
    
#     num_choose = int(input(f"You have {life} attempts remaining to guess the number. \nMake a guess: "))

#     if life <= 1:
#       print ("You lose")
#       end_game = True
#     elif num_choose > guess_number:
#       print ("Too high. You lose.")
#       life -= 1
#       end_game = False
#     elif num_choose < guess_number:
#       print ("Too low. You lose/")
#       life -= 1
#       end_game = False
#     elif num_choose == guess_number:
#       print ("You win")
#       end_game = True

# game()
## END Ver_1

## Ver_2

import random
from art import logo

hard_level = 5
easy_level = 10
#Function to set difficalty
def set_difficalty():
  dif_level = input ("Choose a difficalty. Type 'easy' or 'hard': ").lower()
  if dif_level == "easy":
    return easy_level
  elif dif_level == "hard":
    return hard_level
#Function to check user's answer
def check_answer(num_choose, guess_number, life):
  """Checks answer. Returns the number of lifes."""
  if num_choose > guess_number:
    print ("Too high. You lose.")
    return life - 1
  elif num_choose < guess_number:
    print ("Too low. You lose.")
    return life - 1
  elif num_choose == guess_number:
    print ("You win")

def game_play():
  print (logo)
  print ("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100")
  guess_number = random.randint(1, 100)
  print(f"Pssst. The correct answer is {guess_number}")
  life = set_difficalty()

  num_choose = 0
  while num_choose != guess_number:
    num_choose = int(input(f"You have {life} attempts remaining to guess the number. \nMake a guess: "))

    life = check_answer(num_choose, guess_number, life)

    if life == 0:
      print ("You've run out. You lose")
      return
    elif num_choose != guess_number:
      print ("Guess again")

game_play()
## END Ver_2