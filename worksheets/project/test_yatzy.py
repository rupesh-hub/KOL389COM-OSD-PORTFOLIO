'''
    MIT License
    Copyright (c) 2025 Rupesh Dulal
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import unittest
from Yatzy import Yatzy

class TestYatzy(unittest.TestCase):

    def setUp(self):
        self.game = Yatzy()

    def test_roll_changes_unlocked_dice(self):
        """Test that rolling changes the value of unlocked dice."""
        self.game.dice = [1, 1, 1, 1, 1]
        self.game.locked = [True, False, False, False, True]
        self.game.roll()
        # Dice at index 0 and 4 should remain unchanged
        self.assertEqual(self.game.dice[0], 1)
        self.assertEqual(self.game.dice[4], 1)
        # The others should possibly change (can't assert exact values due to randomness)
        self.assertIn(self.game.dice[1], range(1, 7))
        print("✓ Test rolling dice changes the value of unlocked dice.")

    def test_toggle_lock(self):
        """Test that toggle_lock flips the lock state."""
        self.assertFalse(self.game.locked[2])
        self.game.toggle_lock(2)
        self.assertTrue(self.game.locked[2])
        self.game.toggle_lock(2)
        self.assertFalse(self.game.locked[2])
        print("✓ Test toggle_lock flips the lock state.")

    def test_number_scores(self):
        """Test scoring for ones to sixes."""
        self.game.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.game.ones(), 1)
        self.assertEqual(self.game.twos(), 2)
        self.assertEqual(self.game.threes(), 3)
        self.assertEqual(self.game.fours(), 4)
        self.assertEqual(self.game.fives(), 5)
        self.assertEqual(self.game.sixes(), 0)
        print("✓ Test scoring for ones to sixes.")

    def test_one_pair(self):
        self.game.dice = [2, 3, 3, 4, 5]
        self.assertEqual(self.game.one_pair(), 6)
        print("✓ Test one pair.")

    def test_one_pair_no_pair(self):
        self.game.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.game.one_pair(), 0)
        print("✓ Test one pair no pair.")

    def test_two_pairs(self):
        self.game.dice = [3, 3, 5, 5, 1]
        self.assertEqual(self.game.two_pairs(), 16)
        print("✓ Test two pairs.")

    def test_two_pairs_single_pair_only(self):
        self.game.dice = [3, 3, 4, 1, 2]
        self.assertEqual(self.game.two_pairs(), 0)
        print("✓ Test two pairs single pair only.")

    def test_three_alike(self):
        self.game.dice = [4, 4, 4, 2, 5]
        self.assertEqual(self.game.three_alike(), 12)
        print("✓ Test three alike.")

    def test_three_alike_none(self):
        self.game.dice = [4, 4, 2, 2, 5]
        self.assertEqual(self.game.three_alike(), 0)
        print("✓ Test three alike none.")

    def test_four_alike(self):
        self.game.dice = [6, 6, 6, 6, 1]
        self.assertEqual(self.game.four_alike(), 24)
        print("✓ Test four alike.")

    def test_four_alike_none(self):
        self.game.dice = [6, 6, 6, 5, 5]
        self.assertEqual(self.game.four_alike(), 0)
        print("✓ Test four alike none.")

    def test_small_straight(self):
        self.game.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.game.small_straight(), 15)
        print("✓ Test small straight.")

    def test_small_straight_invalid(self):
        self.game.dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.game.small_straight(), 0)
        print("✓ Test small straight invalid.")

    def test_large_straight(self):
        self.game.dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.game.large_straight(), 20)
        print("✓ Test large straight.")

    def test_large_straight_invalid(self):
        self.game.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.game.large_straight(), 0)
        print("✓ Test large straight invalid.")

    def test_full_house(self):
        self.game.dice = [2, 2, 3, 3, 3]
        self.assertEqual(self.game.full_house(), 13)
        print("✓ Test full house.")

    def test_full_house_invalid(self):
        self.game.dice = [2, 2, 2, 2, 5]  # No 3+2 combo
        self.assertEqual(self.game.full_house(), 0)
        print("✓ Test full house invalid.")

    def test_chance(self):
        self.game.dice = [1, 2, 3, 4, 6]
        self.assertEqual(self.game.chance(), 16)
        print("✓ Test chance.")

    def test_yatzy(self):
        self.game.dice = [4, 4, 4, 4, 4]
        self.assertEqual(self.game.yatzy(), 50)
        print("✓ Test yatzy.")

    def test_yatzy_invalid(self):
        self.game.dice = [4, 4, 4, 4, 5]
        self.assertEqual(self.game.yatzy(), 0)
        print("✓ Test yatzy invalid.")

    def test_str(self):
        self.game.dice = [1, 2, 3, 4, 5]
        self.game.locked = [True, False, True, False, True]
        expected = "Dice: [1, 2, 3, 4, 5] | Locks: [True, False, True, False, True]"
        self.assertEqual(str(self.game), expected)
        print("✓ Test str.")

if __name__ == '__main__':
    unittest.main()
