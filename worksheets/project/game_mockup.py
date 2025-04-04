'''
    MIT License
    Copyright (c) 2025 Rupesh Dulal
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from Yatzy import Yatzy
from collections import defaultdict
import os
import sys
import time

class InteractiveYatzy:
    def __init__(self):
        self.game = Yatzy()
        self.scores = defaultdict(int)
        self.remaining_categories = [
            'ones', 'twos', 'threes', 'fours', 'fives', 'sixes',
            'one_pair', 'two_pairs', 'three_alike', 'four_alike',
            'small_straight', 'large_straight', 'full_house',
            'chance', 'yatzy'
        ]
        self.MAX_ROLLS = 3
        self.current_roll = 0

    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_dice_animation(self):
        """Show rolling animation before revealing dice."""
        print("\nRolling dice...")
        for _ in range(3):
            print("⚁ ⚂ ⚃ ⚄ ⚅", end='\r')
            time.sleep(0.3)
        print(" " * 20, end='\r')  # Clear animation line

    def display_dice(self):
        """Display dice with visual lock indicators."""
        print("\nYour dice:")
        for i, (val, locked) in enumerate(zip(self.game.dice, self.game.locked), 1):
            lock_status = "LOCKED" if locked else "FREE  "
            print(f"  Die {i}: [{val}] - {lock_status}")

    def display_scoreboard(self):
        """Show current scores in a clean format."""
        print("\n" + "="*50)
        print(" " * 18 + "SCOREBOARD")
        print("="*50)
        
        # Upper section
        print("\nUpper Section:")
        upper = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']
        for cat in upper:
            score = self.scores.get(cat, " ")
            print(f"  {cat.title():15}: {score:>3}")
        
        # Lower section
        print("\nLower Section:")
        lower = [
            'one_pair', 'two_pairs', 'three_alike', 'four_alike',
            'small_straight', 'large_straight', 'full_house',
            'chance', 'yatzy'
        ]
        for cat in lower:
            score = self.scores.get(cat, " ")
            print(f"  {cat.replace('_', ' ').title():15}: {score:>3}")
        
        print("="*50)

    def get_dice_to_lock(self):
        """Get which dice player wants to lock/unlock."""
        while True:
            try:
                print("\nWhich dice do you want to toggle? (1-5)")
                print("Enter numbers separated by commas (e.g., '1,3,5')")
                print("Or press Enter to continue without changes")
                choice = input("Your choice: ").strip()
                
                if not choice:
                    return []
                
                indexes = [int(num)-1 for num in choice.split(",") if num.strip().isdigit()]
                if all(0 <= idx < 5 for idx in indexes):
                    return indexes
                print("Please enter numbers between 1 and 5")
            except ValueError:
                print("Invalid input. Please try again.")

    def select_category(self):
        """Let player choose where to apply their score."""
        available = [cat for cat in self.remaining_categories if cat not in self.scores]
        if not available:
            return None

        print("\nAvailable Categories:")
        for i, cat in enumerate(available, 1):
            score = getattr(self.game, cat)()
            print(f"{i}. {cat.replace('_', ' ').title()} (Potential: {score} points)")

        while True:
            try:
                choice = input("\nWhere will you score? (1-{}): ".format(len(available)))
                if not choice.isdigit():
                    raise ValueError
                idx = int(choice) - 1
                if 0 <= idx < len(available):
                    return available[idx]
                raise ValueError
            except ValueError:
                print("Please enter a valid number from the list")

    def play_turn(self):
        """Handle one complete turn (3 rolls)."""
        self.current_roll = 0
        self.game = Yatzy()  # Reset dice and locks
        
        while self.current_roll < self.MAX_ROLLS:
            self.clear_screen()
            print(f"\n=== TURN {self.current_roll + 1}/{self.MAX_ROLLS} ===")
            
            # Roll animation and display
            self.display_dice_animation()
            self.game.roll()
            self.display_dice()
            
            # After first roll, show potential scores
            if self.current_roll > 0:
                print("\nPotential Scores:")
                for cat in self.remaining_categories:
                    if cat not in self.scores:
                        score = getattr(self.game, cat)()
                        print(f"  {cat.replace('_', ' ').title():15}: {score:>2}")
            
            self.current_roll += 1
            
            # Allow locking after each roll except the last
            if self.current_roll < self.MAX_ROLLS:
                to_lock = self.get_dice_to_lock()
                for idx in to_lock:
                    self.game.toggle_lock(idx)
                
                input("\nPress Enter to roll again...")

        # Final scoring
        self.clear_screen()
        print("\n=== FINAL DICE ===")
        self.display_dice()
        
        category = self.select_category()
        if category:
            score = getattr(self.game, category)()
            self.scores[category] = score
            print(f"\nScored {score} points for {category.replace('_', ' ')}!")
            time.sleep(1.5)

    def show_final_score(self):
        """Display complete scoreboard at game end."""
        self.clear_screen()
        print("\n" + "="*50)
        print(" " * 18 + "GAME OVER")
        print("="*50)
        
        # Calculate totals
        upper = sum(self.scores.get(cat, 0) for cat in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes'])
        bonus = 50 if upper >= 63 else 0
        lower = sum(self.scores.get(cat, 0) for cat in [
            'one_pair', 'two_pairs', 'three_alike', 'four_alike',
            'small_straight', 'large_straight', 'full_house',
            'chance', 'yatzy'
        ])
        total = upper + bonus + lower
        
        # Display all scores
        print("\nFINAL SCORES:")
        self.display_scoreboard()
        
        print("\n" + "-"*50)
        print(f"Upper Section Total: {upper}")
        print(f"Bonus:              {bonus}")
        print(f"Lower Section Total: {lower}")
        print("-"*50)
        print(f"GRAND TOTAL:        {total}")
        print("="*50)

    def run(self):
        """Main game loop."""
        try:
            print("Welcome to Console Yatzy!")
            print("Rules:")
            print("- You get 3 rolls per turn")
            print("- Lock dice you want to keep between rolls")
            print("- After 3 rolls, choose where to score")
            input("\nPress Enter to begin...")
            
            while len(self.scores) < len(self.remaining_categories):
                self.play_turn()
            
            self.show_final_score()
            print("\nThanks for playing!")
        except KeyboardInterrupt:
            print("\nGame ended by user.")
            sys.exit(0)

if __name__ == "__main__":
    InteractiveYatzy().run()