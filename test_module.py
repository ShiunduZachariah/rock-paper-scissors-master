import unittest
from RPS_game import play, brian, zach, quincy, shiundu
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("Testing game against quincy...")
        actual = play(player, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat quincy at least 60% of the time.')

    def test_player_vs_zach(self):
        print("Testing game against zach...")
        actual = play(player, zach, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat zach at least 60% of the time.')

    def test_player_vs_shiundu(self):
        print("Testing game against shiundu...")
        actual = play(player, shiundu, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat shiundu at least 60% of the time.')

    def test_player_vs_brian(self):
        print("Testing game against brian...")
        actual = play(player, brian, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat brian at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
