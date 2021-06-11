from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print (logo)
auction = {}

auction_end = False

def winner_bid (auction_name_bids):
  bidder_bid = 0
  winner_name = ""
  for bidder in auction_name_bids:
    some_bid = auction_name_bids[bidder]
    if some_bid > bidder_bid:
      bidder_bid = some_bid
      winner_name = bidder
  print(winner_name)


while not auction_end:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  auction[name] = bid
  ask = input("Are there any other bidders? Type 'yes' or 'no'.")
  if ask == "no":
    auction_end = True
    # winner_bid(auction)
  elif ask == "yes":
    clear()
winner_bid(auction)

### way_2 without def_function
# hi_bid = 0
# winner = ""
# for bidder in auction:
#   bid_amount = auction[name]
#   if bid_amount > hi_bid:
#     hi_bid = bid_amount
#     winner = bidder
# print (winner)