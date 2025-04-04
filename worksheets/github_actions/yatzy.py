"""
Yatzy Game Implementation
Contains the core game logic and scoring rules for a simplified Yatzy game.
"""

from collections import Counter
from typing import List
import random

class Yatzy:
    """Main Yatzy game class handling dice rolls, locks, and scoring."""
    
    def __init__(self):
        """Initialize game with 5 unlocked dice."""
        self.dice = [1] * 5  # Start with all dice showing 1
        self.locked = [False] * 5
        self.roll()  # Initial random roll

    def roll(self) -> None:
        """Roll all unlocked dice with random values (1-6)."""
        self.dice = [random.randint(1, 6) if not self.locked[i] else val 
                    for i, val in enumerate(self.dice)]

    def toggle_lock(self, index: int) -> None:
        """Toggle lock state for a specific die (0-based index)."""
        if 0 <= index < 5:
            self.locked[index] = not self.locked[index]

    # ----------------------
    # Scoring Methods
    # ----------------------

    def _sum_numbers(self, number: int) -> int:
        """Helper: Sum all dice showing specific number."""
        return sum(die for die in self.dice if die == number)

    def ones(self) -> int: return self._sum_numbers(1)
    def twos(self) -> int: return self._sum_numbers(2)
    def threes(self) -> int: return self._sum_numbers(3)
    def fours(self) -> int: return self._sum_numbers(4)
    def fives(self) -> int: return self._sum_numbers(5)
    def sixes(self) -> int: return self._sum_numbers(6)

    def _counts(self) -> List[int]:
        """Get counts of each die value (1-6)."""
        return Counter(self.dice)

    def one_pair(self) -> int:
        """Highest pair score (0 if no pair)."""
        counts = self._counts()
        return max((val * 2 for val, cnt in counts.items() if cnt >= 2), default=0)

    def two_pairs(self) -> int:
        """Sum of two highest pairs (0 if <2 pairs)."""
        pairs = [val * 2 for val, cnt in self._counts().items() if cnt >= 2]
        return sum(sorted(pairs, reverse=True)[:2]) if len(pairs) >= 2 else 0

    def three_alike(self) -> int:
        """Highest three-of-a-kind score."""
        counts = self._counts()
        return max((val * 3 for val, cnt in counts.items() if cnt >= 3), default=0)

    def four_alike(self) -> int:
        """Highest four-of-a-kind score."""
        counts = self._counts()
        return max((val * 4 for val, cnt in counts.items() if cnt >= 4), default=0)

    def small_straight(self) -> int:
        """15 if dice show 1-5, else 0."""
        return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0

    def large_straight(self) -> int:
        """20 if dice show 2-6, else 0."""
        return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def full_house(self) -> int:
        """Sum of all dice if full house (3+2), else 0."""
        counts = list(self._counts().values())
        return sum(self.dice) if (3 in counts and 2 in counts) else 0

    def chance(self) -> int:
        """Sum of all dice."""
        return sum(self.dice)

    def yatzy(self) -> int:
        """50 if all dice match, else 0."""
        return 50 if len(set(self.dice)) == 1 else 0

    def __str__(self) -> str:
        """String representation of current game state."""
        return f"Dice: {self.dice} | Locks: {self.locked}"