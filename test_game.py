import unittest 
from game import Game
from player import Player

class TestPlayer(unittest.TestCase):
    
    def test_instance(self): 
        game = Game()

        self.assertIsInstance(game, Game)
        self.assertIsInstance(game.player_one, Player)
        self.assertIsInstance(game.player_two, Player)
        self.assertEqual(game.game_mode, None)

    def test_display_welcome(self):
        game = Game()
        game.display_welcome()
        input = ['1', '2']

        self.assertIn(game.game_mode, input)

    def test_choose_winner(self):
        game = Game()
        game.choose_winner("Rock","Paper")

        self.assertEqual(game.player_one.score, 0)
        self.assertEqual(game.player_two.score, 1)


if __name__ == '__main__': 
    unittest.main()
