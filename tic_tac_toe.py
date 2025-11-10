#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
A classic 3x3 grid game for two players.
Players take turns placing X and O marks to get three in a row.
"""

import os
import sys

class TicTacToe:
    def __init__(self):
        """Initialize the game with an empty 3x3 board."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        
    def display_board(self):
        """Display the current state of the game board."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*30)
        print("    TIC-TAC-TOE GAME")
        print("="*30)
        print(f"   Current Player: {self.current_player}")
        print("-"*30)
        print("   Position Guide:")
        print("   1 | 2 | 3")
        print("  ---|---|---")
        print("   4 | 5 | 6") 
        print("  ---|---|---")
        print("   7 | 8 | 9")
        print("-"*30)
        print("   Current Board:")
        
        for i in range(3):
            row = f"   {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}"
            print(row)
            if i < 2:
                print("  ---|---|---")
        print("-"*30)
        
    def get_position_from_number(self, num):
        """Convert position number (1-9) to row, col coordinates."""
        num -= 1  # Convert to 0-based indexing
        row = num // 3
        col = num % 3
        return row, col
        
    def is_valid_move(self, position):
        """Check if the move is valid (position is empty and in range)."""
        if position < 1 or position > 9:
            return False, "Position must be between 1 and 9!"
            
        row, col = self.get_position_from_number(position)
        if self.board[row][col] != ' ':
            return False, "Position already taken!"
            
        return True, ""
        
    def make_move(self, position):
        """Make a move on the board."""
        row, col = self.get_position_from_number(position)
        self.board[row][col] = self.current_player
        
    def check_winner(self):
        """Check if there's a winner or if the game is a tie."""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
                
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
            
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
            
        # Check for tie (board full)
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'TIE'
            
        return None
        
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
    def play_game(self):
        """Main game loop."""
        print("\n" + "="*40)
        print("   WELCOME TO TIC-TAC-TOE!")
        print("="*40)
        print("   Instructions:")
        print("   - Players alternate between X and O")
        print("   - Enter a number (1-9) to place your mark")
        print("   - Get 3 in a row to win!")
        print("   - Press Enter to start...")
        input()
        
        while not self.game_over:
            self.display_board()
            
            # Get player input
            try:
                position = input(f"\n   Player {self.current_player}, enter position (1-9) or 'q' to quit: ").strip()
                
                if position.lower() == 'q':
                    print("\n   Thanks for playing! Goodbye!")
                    return
                    
                position = int(position)
                
                # Validate and make move
                valid, message = self.is_valid_move(position)
                if not valid:
                    print(f"\n   {message}")
                    input("   Press Enter to continue...")
                    continue
                    
                self.make_move(position)
                
                # Check for winner
                result = self.check_winner()
                if result:
                    self.display_board()
                    if result == 'TIE':
                        print("\n" + "="*30)
                        print("     IT'S A TIE!")
                        print("     Good game!")
                        print("="*30)
                    else:
                        print("\n" + "="*30)
                        print(f"     PLAYER {result} WINS!")
                        print("     Congratulations!")
                        print("="*30)
                    self.game_over = True
                    self.winner = result
                else:
                    # Switch to other player
                    self.switch_player()
                    
            except ValueError:
                print("\n   Please enter a valid number (1-9) or 'q' to quit!")
                input("   Press Enter to continue...")
            except KeyboardInterrupt:
                print("\n\n   Game interrupted. Goodbye!")
                return
                
        # Ask if they want to play again
        self.ask_play_again()
        
    def ask_play_again(self):
        """Ask if players want to play again."""
        while True:
            try:
                choice = input("\n   Play again? (y/n): ").strip().lower()
                if choice in ['y', 'yes']:
                    self.reset_game()
                    self.play_game()
                    break
                elif choice in ['n', 'no']:
                    print("\n   Thanks for playing! Goodbye!")
                    break
                else:
                    print("   Please enter 'y' for yes or 'n' for no.")
            except KeyboardInterrupt:
                print("\n\n   Goodbye!")
                break
                
    def reset_game(self):
        """Reset the game for a new round."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

def main():
    """Main function to run the Tic-Tac-Toe game."""
    try:
        game = TicTacToe()
        game.play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()