# Backgammon Game Using Monte Carlo and MCTS

## Overview
This project analyzes the Backgammon game using two search algorithms: Monte Carlo Search (MC) and Monte Carlo Tree Search (MCTS). The goal is to compare the performance of these algorithms in finding optimal moves and evaluating their efficiency.

## Key Features
- **Backgammon State Representation**: Encapsulates the board configuration, bar positions, and off positions for both players.
- **Monte Carlo Search (MC)**: Performs random simulations to estimate the value of possible moves.
- **Monte Carlo Tree Search (MCTS)**: Combines exploration and exploitation to find the optimal move.
- **Heuristic Simulation**: Evaluates the outcome of a game using a simple heuristic approach.
- **Comparison**: Runs a series of games to compare MC and MCTS in terms of wins and execution time.

## Project Structure
- `backgammon_state.py`: Defines the `BackgammonState` class and initializes the board.
- `monte_carlo.py`: Implements the Monte Carlo Search algorithm.
- `mcts.py`: Implements the Monte Carlo Tree Search algorithm.
- `utils.py`: Contains utility functions for heuristic simulation and comparison.
- `main.py`: Runs the comparison between MC and MCTS.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/backgammon-analysis.git
   cd backgammon-analysis
   ```

2. Ensure Python is installed on your system.


## Usage
Run the comparison script:
   ```bash
    python main.py
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

