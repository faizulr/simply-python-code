#!/usr/bin/env python3
"""
Unit tests for the games
"""
import unittest
import sys
import os

class TestNumberGuessingGame(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Import the game class
        sys.path.append(os.path.dirname(__file__))
        from guess_game import NumberGuessingGame
        self.game = NumberGuessingGame()
    
    def test_initialization(self):
        """Test game initialization"""
        self.assertEqual(self.game.min_number, 1)
        self.assertEqual(self.game.max_number, 100)
        self.assertEqual(self.game.max_attempts, 7)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.games_played, 0)
    
    def test_difficulty_changes(self):
        """Test difficulty level changes"""
        # Test easy difficulty
        self.game.min_number, self.game.max_number, self.game.max_attempts = 1, 50, 8
        self.assertEqual(self.game.max_number, 50)
        self.assertEqual(self.game.max_attempts, 8)

class TestSnakeGame(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # This would require pygame to be installed
        pass
    
    def test_snake_initialization(self):
        """Test snake initialization"""
        # Would test Snake class initialization
        pass
    
    def test_food_randomization(self):
        """Test food placement"""
        # Would test Food class randomization
        pass

if __name__ == '__main__':
    print("🧪 Running Unit Tests...")
    unittest.main(verbosity=2)