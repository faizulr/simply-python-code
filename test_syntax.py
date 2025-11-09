#!/usr/bin/env python3
"""
Quick syntax and import test for the games
"""

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import pygame
        print("✅ Pygame imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import pygame: {e}")
        return False

def test_syntax():
    """Test if game files have valid Python syntax"""
    import ast
    
    files_to_test = ['snake_game.py', 'guess_game.py']
    
    for filename in files_to_test:
        try:
            with open(filename, 'r') as f:
                content = f.read()
            
            # Parse the file to check syntax
            ast.parse(content)
            print(f"✅ {filename} - Syntax OK")
            
        except SyntaxError as e:
            print(f"❌ {filename} - Syntax Error: {e}")
            return False
        except FileNotFoundError:
            print(f"❌ {filename} - File not found")
            return False
    
    return True

def test_basic_functionality():
    """Test basic functionality without running full games"""
    try:
        # Test number guessing game logic
        import random
        test_number = random.randint(1, 100)
        print(f"✅ Random number generation works: {test_number}")
        
        # Test basic pygame initialization (without display)
        import pygame
        pygame.init()
        print("✅ Pygame initialization works")
        pygame.quit()
        
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Running Game Tests...")
    print("-" * 40)
    
    all_tests_passed = True
    
    # Run tests
    all_tests_passed &= test_imports()
    all_tests_passed &= test_syntax() 
    all_tests_passed &= test_basic_functionality()
    
    print("-" * 40)
    if all_tests_passed:
        print("🎉 All tests passed! Games should work.")
        print("\nTo run the games:")
        print("python snake_game.py")
        print("python guess_game.py")
    else:
        print("❌ Some tests failed. Check the errors above.")