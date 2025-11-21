# Python Game & Utility Collection

A collection of Python console games and utilities, some with GUI (Pygame).

## Games
- **Snake Game** (`snake_game.py`): Classic snake game with arrow key controls (Pygame GUI)
- **Number Guessing Game** (`guess_game.py`): Console-based guessing game
- **Sum Game** (`sum_game.py`): Console-based arithmetic practice with ten random addition problems
- **Tic-Tac-Toe** (`tic_tac_toe.py`): Classic 3x3 grid game for two players

## Utilities & Tools
- **Fibonacci Generator** (`fibonacci_generator.py`): Generates Fibonacci series up to a specified number of digits
- **Random Sum Generator** (`random_sum_generator.py`): Generates and sums a user-specified number of random integers
- **Basic Calculator** (`basic_calculator.py`): Add, subtract, multiply, and divide two numbers
- **Number Sequence Predictor** (`number_predictor.py`): Predicts the next number in a 3-number sequence using pattern recognition


## Requirements
- Python 3.7+
- Pygame library (*only required for Snake Game*)

## Installation
```bash
pip install pygame
```

## How to Run
```bash
# Snake Game (GUI)
python snake_game.py

# Number Guessing Game (Console)
python guess_game.py

# Sum Game (Console)
python sum_game.py

# Tic-Tac-Toe Game (Console)
python tic_tac_toe.py

# Fibonacci Generator (Console)
python fibonacci_generator.py

# Random Sum Generator (Console)
python random_sum_generator.py

# Basic Calculator (Console)
python basic_calculator.py

# Number Sequence Predictor (Console)
python number_predictor.py
```

## Controls
- **Snake Game**: Use arrow keys to move, avoid walls and yourself
- **Number Guessing Game**: Follow console prompts
- **Sum Game**: Enter the correct sum for each prompt; ten rounds per session
- **Tic-Tac-Toe**: Enter numbers 1-9 to place your mark, players alternate turns

## Features
- Score tracking (for relevant games)
- Game over detection
- Restart functionality
