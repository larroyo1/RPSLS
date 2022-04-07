import unittest 
from player import Player
from gesture import Gesture

class TestPlayer(unittest.TestCase):
    
    def test_instance(self): 
        player = Player('Player 1')

        self.assertIsInstance(player, Player)
        self.assertEqual(player.name, 'Player 1')
        self.assertEqual(player.score, 0)
        
        for gesture in player.gestures: 
            self.assertIsInstance(gesture, Gesture)

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
        player = Player('Sheldon')
        user_input = player.choose_something(player.characters, 'character')
        player.current_gesture = player.gestures[int(user_input)]
        
        self.assertIn(player.name, player.characters)

if __name__ == '__main__': 
    unittest.main()
