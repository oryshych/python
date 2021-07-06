from art import logo, vs
from game_data import data
import random
from replit import clear 

def get_random_data():
  """Get random data from game_data"""
  return random.choice(data)

def format_data(account):
  """Format data to print"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Check users answer""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_data()
  account_b = get_random_data()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_data()

    while account_a == account_b:
      account_b = get_random_data()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

# Take random data A and B

# Format data to print

# Ask User A or B

# Check users answer. Get 'follower_count'

# Feedback

# Score game

# Repeat game if user win

# Make B to A in next step

# Clear screen in next round of game