import unittest 
from player import Player

class TestPlayer(unittest.TestCase):
    
    def test_instance(self): 
        player = Player('Player 1')

        self.assertIsInstance(player, Player)
        self.assertEqual(player.name, 'Player 1')
        self.assertEqual(player.score, 0)
        self.assertEqual(player.gestures, ["Rock","Paper","Scissors","Lizard","Spock"])
        self.assertEqual(player.current_gesture, None)
        self.assertEqual(player.characters, ['Sheldon','Leonard','Penny','Amy Farrah Fowler','Bernadette','Wolowitz'])
        

    def test_choose_gesture(self): 
        player = Player('Player 1')
        player.choose_gesture()

        self.assertIn(player.current_gesture, player.gestures)

    def test_choose_character(self): 
        player = Player('Player')
        player.choose_character()

        self.assertIn(player.name, player.characters)

    def test_choose_something(self):
        player = Player('Player 1')
        user_input = player.choose_something(player.gestures, 'gesture')
        player.current_gesture = player.gestures[int(user_input)]
        
        self.assertIn(player.current_gesture, player.gestures)


if __name__ == '__main__': 
    unittest.main()
