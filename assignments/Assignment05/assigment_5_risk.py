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
def get_quality_score(num_scores):
    # Create an empty list to save grades
    scores = []
    
    # Generate num_scores ratings from 1 to 6
    for _ in range(num_scores):
        score = random.randint(1, 6)  # Random number from 1 to 6
        scores.append(score)  # Add score to the list
    
    # Sorting the scores in descending order
    scores_sorted = sorted(scores, reverse=True)

    # Return sorted list of grades
    return scores_sorted  


# Feature simulates single round of competition between two establishments
def simulate_round():
    # "Hot Potato Haven" receives 3 marks for quality
    quality_a = get_quality_score(3)
    # "Potato Empire" also receives 3 marks for quality
    quality_b = get_quality_score(3)
    
    # Initial wins per round for each establishment
    wins_a = 0
    wins_b = 0
    
    # Сompare the results of assessments for each place
    for i in range(3):  # Each institution has 3 ratings
        if quality_a[i] > quality_b[i]:
            wins_a += 1  # "Hot Potato Haven" wins one point
        elif quality_a[i] < quality_b[i]:
            wins_b += 1  # "Potato Empire" wins one point
    
    return wins_a, wins_b


# Define vatiables
total_wins_a = 0 # Total wins for "Hot Potato Haven" 
total_wins_b = 0 # Total wins for "Potato Empire" 
rounds_played = 0 # Number of Rounds Counter

# The competition continues until one of the establishments reaches 10 wins
while total_wins_a < 10 and total_wins_b < 10:
    rounds_played += 1
    wins_a, wins_b = simulate_round() # Function simulation round
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

# Plotting graph
labels = ['Hot Potato Haven', 'Potato Empire']
total_wins = [total_wins_a, total_wins_b]

# Graph of results
plt.figure(figsize=(8, 5))
plt.bar(labels, total_wins, color=['orange', 'green'])
plt.title('Results of the Fried Potato Competition')
plt.xlabel('Institutions')
plt.ylabel('Total number of wins')
plt.show()