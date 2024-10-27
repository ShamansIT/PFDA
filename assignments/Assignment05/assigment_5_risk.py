# Risk of going hungry simmulation

"""
Since the topic of troops and wars is currently causing me anxiety and stress, and as a result,
the loss of inspiration to solve this particular problem, with your permission, 
I would like to choose a different essence of the program, let's say it will be a competition between 
two food establishments for the preparation of fried potatoes. 
I hope this will not be counted as a mistake or incorrect completion of the task.
"""

import random
import matplotlib.pyplot as plt 

# Function to get a random quality score for each institution
def simulate_round():
    pass



# Define vatiables
total_wins_a = 0 # Total wins for "Hot Potato Haven" 
total_wins_b = 0 # Total wins for "Potato Empire" 
rounds_played = 0 # Number of Rounds Counter

# The competition continues until one of the establishments reaches 10 wins
while total_wins_a < 10 and total_wins_b < 10:
    rounds_played += 1
    wins_a, wins_b = simulate_round() # function simulation round
    total_wins_a += wins_a
    total_wins_b += wins_b

    # Information about round
    print(f"Round {rounds_played}: Hot Potato Haven - {wins_a} Wins, Potato Empire - {wins_b} Wins")

# Define winner
if total_wins_a >= 10:
    winner = "Hot Potato Haven"
else:
    winner = "Potato Empire"

print(f"\nWinner: {winner} after {rounds_played} rounds!")