import random
import sys

class NumberGuessingGame:
    def __init__(self):
        self.min_number = 1
        self.max_number = 100
        self.max_attempts = 7
        self.score = 0
        self.games_played = 0
        
    def play_game(self):
        """Play a single round of the guessing game"""
        secret_number = random.randint(self.min_number, self.max_number)
        attempts = 0
        
        print(f"\n🎮 Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}")
        print(f"You have {self.max_attempts} attempts to guess it!")
        print("-" * 50)
        
        while attempts < self.max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}/{self.max_attempts} - Enter your guess: "))
                attempts += 1
                
                if guess < self.min_number or guess > self.max_number:
                    print(f"⚠️  Please enter a number between {self.min_number} and {self.max_number}")
                    continue
                
                if guess == secret_number:
                    points = self.max_attempts - attempts + 1
                    self.score += points
                    self.games_played += 1
                    print(f"\n🎉 Congratulations! You guessed it!")
                    print(f"The number was {secret_number}")
                    print(f"You earned {points} points!")
                    return True
                
                elif guess < secret_number:
                    print("📈 Too low! Try a higher number.")
                    self.give_hint(guess, secret_number, attempts)
                    
                else:
                    print("📉 Too high! Try a lower number.")
                    self.give_hint(guess, secret_number, attempts)
                    
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
                continue
        
        # Game over - ran out of attempts
        self.games_played += 1
        print(f"\n💀 Game Over! You've used all {self.max_attempts} attempts.")
        print(f"The number was {secret_number}")
        return False
    
    def give_hint(self, guess, secret_number, attempts):
        """Provide helpful hints based on how close the guess is"""
        difference = abs(guess - secret_number)
        
        if attempts >= 3:  # Give hints after 3 attempts
            if difference <= 5:
                print("🔥 Very close!")
            elif difference <= 15:
                print("🌡️  Getting warmer...")
            elif difference <= 30:
                print("❄️  Getting colder...")
            else:
                print("🧊 Very cold!")
    
    def show_statistics(self):
        """Display game statistics"""
        if self.games_played > 0:
            print(f"\n📊 Your Statistics:")
            print(f"Games played: {self.games_played}")
            print(f"Total score: {self.score}")
            print(f"Average score: {self.score / self.games_played:.1f}")
        else:
            print("No games played yet!")
    
    def change_difficulty(self):
        """Allow player to change game difficulty"""
        print("\n🎯 Choose difficulty level:")
        print("1. Easy (1-50, 8 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 6 attempts)")
        print("4. Expert (1-500, 5 attempts)")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                self.min_number, self.max_number, self.max_attempts = 1, 50, 8
                print("✅ Difficulty set to Easy")
            elif choice == 2:
                self.min_number, self.max_number, self.max_attempts = 1, 100, 7
                print("✅ Difficulty set to Medium")
            elif choice == 3:
                self.min_number, self.max_number, self.max_attempts = 1, 200, 6
                print("✅ Difficulty set to Hard")
            elif choice == 4:
                self.min_number, self.max_number, self.max_attempts = 1, 500, 5
                print("✅ Difficulty set to Expert")
            else:
                print("❌ Invalid choice. Keeping current difficulty.")
                
        except ValueError:
            print("❌ Invalid input. Keeping current difficulty.")
    
    def main_menu(self):
        """Display main menu and handle user choices"""
        while True:
            print("\n" + "="*50)
            print("🎲 NUMBER GUESSING GAME")
            print("="*50)
            print("1. 🎮 Play Game")
            print("2. 🎯 Change Difficulty")
            print("3. 📊 Show Statistics")
            print("4. 🚪 Quit")
            print("-"*50)
            
            try:
                choice = int(input("Enter your choice (1-4): "))
                
                if choice == 1:
                    result = self.play_game()
                    if result:
                        print("\n🎊 Well done!")
                    else:
                        print("\n💪 Better luck next time!")
                
                elif choice == 2:
                    self.change_difficulty()
                
                elif choice == 3:
                    self.show_statistics()
                
                elif choice == 4:
                    print("\n👋 Thanks for playing! Goodbye!")
                    self.show_statistics()
                    sys.exit()
                
                else:
                    print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
                    
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\n\n👋 Game interrupted. Goodbye!")
                sys.exit()

def main():
    """Main function to start the game"""
    game = NumberGuessingGame()
    game.main_menu()

if __name__ == "__main__":
    main()