# Demographic Analysis Research

## Overview

This project simulates a friendly competition between two food establishments—**Hot Potato Haven** and **Potato Empire**—to determine who can prepare the best fried potatoes. The program uses Python to model the competition and generates a bar chart to visualize the results.

---

## Simulation Description

### Rules of the Competition:
1. Both establishments receive 3 random quality scores (from 1 to 6) for each round.
2. The quality scores are compared, and the establishment with the higher score in a round earns a point.
3. The competition continues until one of the establishments accumulates at least 10 total points.

### Output:
- Round-by-round results displayed in the console.
- Final winner after all rounds.
- A bar chart illustrating the total wins for each establishment.

---

## How It Works

### Key Functions:
1. `get_quality_score(num_scores)`: 
   - Generates a list of random quality scores for each establishment.
   - Sorts and returns the scores in descending order.

2. `simulate_round()`: 
   - Simulates a single round of competition.
   - Compares quality scores and updates win counts for each establishment.

3. Main loop:
   - Repeats the competition until one establishment wins at least 10 rounds.

### Visualization:
- A bar chart generated using Matplotlib showcases the final scores.

---

## Setup

### Requirements:
- Python 3.x
- Libraries:
  - `random` (built-in)
  - `matplotlib`

### Running the Program:
1. Save the script as `assignment_5_risk.py`.
2. Run the script:
   ```bash
   python assignment_5_risk.py
   ```
3. Observe the round-by-round results in the console.
4. View the bar chart for final scores.

---

## Learning Objectives

1. **Programming Skills**:
   - Implement loops, conditional statements, and function calls.
   - Handle randomness and comparisons in Python.
2. **Data Visualization**:
   - Utilize Matplotlib to create a bar chart of results.
3. **Creative Thinking**:
   - Adapt a generic simulation framework for a lighthearted, fun competition.

---

## Example Output

### Console Output:
```plaintext
Round 1: Hot Potato Haven - 2 Wins, Potato Empire - 1 Wins
Round 2: Hot Potato Haven - 1 Wins, Potato Empire - 2 Wins
...
Winner: Potato Empire after 8 rounds!
```

### Bar Chart:
A visually appealing bar chart comparing total wins for both establishments.

---

## References
1. Python Random Documentation: [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)
2. Python Matplotlib Documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
