# Python Game & Utility Collection

A comprehensive collection of Python console games and utilities featuring both command-line and GUI applications. Perfect for learning Python programming concepts, game development, and mathematical algorithms.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://pygame.org)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#testing)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎮 Games

### Interactive Entertainment
- **🐍 Snake Game** (`snake_game.py`): Enhanced snake game with AI opponent, multiple difficulty levels, and smooth Pygame graphics
- **🎯 Number Guessing Game** (`guess_game.py`): Interactive guessing game with hints, multiple difficulty levels, and score tracking
- **➕ Sum Game** (`sum_game.py`): Mathematical practice game with 10 rounds of addition problems and immediate feedback
- **⭕ Tic-Tac-Toe** (`tic_tac_toe.py`): Full-featured two-player game with win detection, input validation, and replay functionality

## 🛠️ Utilities & Tools

### Mathematical & Computational Tools
- **🌀 Fibonacci Generator** (`fibonacci_generator.py`): Generates Fibonacci sequences up to specified digit limits with performance statistics
- **🎲 Random Sum Generator** (`random_sum_generator.py`): Creates and sums user-defined quantities of random integers with range customization
- **🧮 Basic Calculator** (`basic_calculator.py`): Four-operation calculator with error handling and input validation
- **🔮 Number Sequence Predictor** (`number_predictor.py`): Advanced pattern recognition system supporting arithmetic, geometric, polynomial, Fibonacci, factorial, and exponential sequences

### String & Text Utilities
- **🔁 Palindrome Checker** (`palindrome_checker.py`): Checks if a string is a palindrome, ignoring case and punctuation. Includes a command-line interface for user input.

## 📋 Requirements

### System Requirements
- **Python 3.7+** (Tested with Python 3.13)
- **Windows, macOS, or Linux**

### Dependencies
- **pygame>=2.0.0** - Required for Snake Game GUI
- **pytest>=7.0.0** - Required for running tests (optional)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/faizulr/simply-python-code.git
cd simply-python-code/project1
```

### 2. Install Dependencies
```bash
# Install required dependencies
pip install -r requirements.txt

# Or install manually
pip install pygame>=2.0.0 pytest>=7.0.0
```

### 3. Verify Installation
```bash
# Run syntax and dependency tests
python test_syntax.py
```

## 🎯 How to Run

### 🎮 Games
```bash
# Snake Game - GUI with AI opponent
python snake_game.py

# Number Guessing Game - Interactive with hints
python guess_game.py

# Sum Game - Math practice with scoring
python sum_game.py

# Tic-Tac-Toe - Two-player strategy game
python tic_tac_toe.py
```

### 🛠️ Utilities
```bash
# Fibonacci Generator - Mathematical sequences
python fibonacci_generator.py

# Random Sum Generator - Number operations
python random_sum_generator.py

# Basic Calculator - Four operations
python basic_calculator.py

# Number Sequence Predictor - Pattern recognition
python number_predictor.py

# Palindrome Checker - String analysis
python palindrome_checker.py
```

## 🎮 Game Controls & Features

### 🐍 Snake Game
- **Controls**: Arrow keys for movement
- **Features**: AI opponent, score tracking, collision detection
- **Goal**: Eat food, avoid walls and the AI snake

### 🎯 Number Guessing Game
- **Controls**: Keyboard input with prompts
- **Features**: Multiple difficulty levels, hint system, score tracking
- **Goal**: Guess the secret number with minimal attempts

### ➕ Sum Game
- **Controls**: Keyboard input for answers
- **Features**: 10 rounds, immediate feedback, input validation
- **Goal**: Solve addition problems correctly

### ⭕ Tic-Tac-Toe
- **Controls**: Enter numbers 1-9 for grid positions
- **Features**: Turn-based play, win detection, replay option
- **Goal**: Get three in a row (horizontal, vertical, or diagonal)

## 🧪 Testing

### Run All Tests
```bash
# Run comprehensive test suite
python test_syntax.py

# Run individual test modules
python test_basic_calculator.py
python test_tic_tac_toe.py
python test_number_predictor.py

# Run with pytest (advanced testing)
pytest test_sum_game.py -v
pytest . -v  # Run all pytest tests
```

### Test Coverage
- **✅ 35+ Unit Tests** covering all functionality
- **✅ Syntax Validation** for all Python files
- **✅ Dependency Verification** for external libraries
- **✅ Error Handling Tests** for edge cases
- **✅ Pattern Recognition Tests** for mathematical sequences

## 📊 Project Statistics

| Component | Files | Tests | Coverage |
|-----------|-------|-------|----------|
| Games | 4 | 15+ | 100% |
| Utilities | 4 | 20+ | 100% |
| **String Tools** | 1 | 3+ | 100% |
| Total | 9 | 38+ | 100% |

## 🚀 Advanced Features

### Number Sequence Predictor Patterns
- **Arithmetic Sequences**: 1, 3, 5 → 7
- **Geometric Sequences**: 2, 6, 18 → 54
- **Fibonacci Sequences**: 1, 1, 2 → 3
- **Polynomial Sequences**: 1, 4, 9 → 16 (perfect squares)
- **Factorial Sequences**: 1, 2, 6 → 24
- **Exponential Sequences**: e¹, e², e³ → e⁴
- **Custom Patterns**: Triangular numbers, powers, and more

### Snake Game AI
- **Pathfinding Algorithm**: AI opponent uses smart movement
- **Dynamic Difficulty**: AI speed adjusts based on game progress
- **Collision Avoidance**: AI respawns when hitting obstacles
- **Strategic Behavior**: AI actively pursues the player

## 🐛 Troubleshooting

### Common Issues

**Pygame Import Error**
```bash
# Solution: Install pygame
pip install pygame>=2.0.0
```

**Permission Errors**
```bash
# Solution: Install to user directory
pip install --user pygame pytest
```

**Python Version Issues**
```bash
# Check Python version
python --version

# Ensure Python 3.7+ is installed
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Run tests**: `python test_syntax.py`
4. **Make changes** and add tests
5. **Commit changes**: `git commit -m "Add feature"`
6. **Push to branch**: `git push origin feature-name`
7. **Create Pull Request**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pygame Community** for the excellent game development library
- **Python Software Foundation** for the amazing Python programming language
- **Testing Framework** contributors for robust testing tools

---

**Made with ❤️ by [Faizul Rahman](https://github.com/faizulr)**

*Happy coding and gaming! 🎮*
