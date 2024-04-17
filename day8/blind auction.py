# blind auction

import os

bids = {}  # define bidding info dictionary
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    
    # bidding_record = {"AAA": 123, "BBB": 456}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished: 
    
    bidder_name = input("What is your name? ")
    bidding_price = int(input("What is your bidding price? $"))
    
    # add {name : price} (using dictionary)
    bids[bidder_name] = bidding_price

    # checking bidders is left? 
    should_continue = input("Are there any bidders? 'yes' or 'no'")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls')  # clear the screen before input name and bid 


 
# 4.2 ___no___

    # find highest bid price
    
    
    # declare the winner
