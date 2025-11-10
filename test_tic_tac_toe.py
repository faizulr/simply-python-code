#!/usr/bin/env python3
"""
Test file for Tic-Tac-Toe game
Tests the core game logic and functionality
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project directory to the path to import the game
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """Test cases for the TicTacToe class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.game = TicTacToe()
    
    def test_initial_board_state(self):
        """Test that the board is initialized correctly."""
        expected_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, expected_board)
        self.assertEqual(self.game.current_player, 'X')
        self.assertFalse(self.game.game_over)
        self.assertIsNone(self.game.winner)
    
    def test_get_position_from_number(self):
        """Test position number to coordinate conversion."""
        test_cases = [
            (1, (0, 0)), (2, (0, 1)), (3, (0, 2)),
            (4, (1, 0)), (5, (1, 1)), (6, (1, 2)),
            (7, (2, 0)), (8, (2, 1)), (9, (2, 2))
        ]
        
        for position, expected in test_cases:
            with self.subTest(position=position):
                result = self.game.get_position_from_number(position)
                self.assertEqual(result, expected)
    
    def test_valid_move_validation(self):
        """Test move validation logic."""
        # Test valid moves
        valid, message = self.game.is_valid_move(5)
        self.assertTrue(valid)
        self.assertEqual(message, "")
        
        # Test invalid position (out of range)
        valid, message = self.game.is_valid_move(0)
        self.assertFalse(valid)
        self.assertEqual(message, "Position must be between 1 and 9!")
        
        valid, message = self.game.is_valid_move(10)
        self.assertFalse(valid)
        self.assertEqual(message, "Position must be between 1 and 9!")
        
        # Test position already taken
        self.game.make_move(5)  # Place X at position 5
        valid, message = self.game.is_valid_move(5)
        self.assertFalse(valid)
        self.assertEqual(message, "Position already taken!")
    
    def test_make_move(self):
        """Test making moves on the board."""
        self.game.make_move(5)  # Center position
        self.assertEqual(self.game.board[1][1], 'X')
        
        self.game.switch_player()
        self.game.make_move(1)  # Top-left corner
        self.assertEqual(self.game.board[0][0], 'O')
    
    def test_switch_player(self):
        """Test player switching functionality."""
        self.assertEqual(self.game.current_player, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')
    
    def test_check_winner_rows(self):
        """Test winner detection for rows."""
        # Test top row win for X
        self.game.board[0] = ['X', 'X', 'X']
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test middle row win for O
        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game.board[1] = ['O', 'O', 'O']
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Test bottom row win for X
        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game.board[2] = ['X', 'X', 'X']
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_columns(self):
        """Test winner detection for columns."""
        # Test left column win for X
        self.game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test middle column win for O
        self.game.board = [[' ', 'O', ' '], [' ', 'O', ' '], [' ', 'O', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Test right column win for X
        self.game.board = [[' ', ' ', 'X'], [' ', ' ', 'X'], [' ', ' ', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_diagonals(self):
        """Test winner detection for diagonals."""
        # Test main diagonal win for X
        self.game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test anti-diagonal win for O
        self.game.board = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_check_winner_tie(self):
        """Test tie detection when board is full."""
        # Create a tie scenario
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertEqual(self.game.check_winner(), 'TIE')
    
    def test_check_winner_no_winner(self):
        """Test when there's no winner yet."""
        # Partially filled board with no winner
        self.game.board = [
            ['X', 'O', ' '],
            [' ', 'X', ' '],
            [' ', ' ', 'O']
        ]
        self.assertIsNone(self.game.check_winner())
    
    def test_reset_game(self):
        """Test game reset functionality."""
        # Make some moves and change game state
        self.game.make_move(5)
        self.game.switch_player()
        self.game.make_move(1)
        self.game.game_over = True
        self.game.winner = 'X'
        
        # Reset the game
        self.game.reset_game()
        
        # Verify everything is reset
        expected_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, expected_board)
        self.assertEqual(self.game.current_player, 'X')
        self.assertFalse(self.game.game_over)
        self.assertIsNone(self.game.winner)
    
    def test_full_game_scenario(self):
        """Test a complete game scenario."""
        # Simulate a game where X wins with top row
        moves = [
            (1, 'X'), (4, 'O'),  # X: top-left, O: middle-left
            (2, 'X'), (5, 'O'),  # X: top-middle, O: center
            (3, 'X')             # X: top-right (wins!)
        ]
        
        for position, expected_player in moves:
            self.assertEqual(self.game.current_player, expected_player)
            valid, _ = self.game.is_valid_move(position)
            self.assertTrue(valid)
            
            self.game.make_move(position)
            
            winner = self.game.check_winner()
            if winner:
                self.assertEqual(winner, 'X')
                break
            else:
                self.game.switch_player()

if __name__ == '__main__':
    unittest.main()