import unittest 
from gesture import Gesture

class TestPlayer(unittest.TestCase):
    
    def test_instance(self): 
        gesture = Gesture('Rock')

        self.assertIsInstance(gesture, Gesture)
        self.assertEqual(gesture.name, 'Rock')
    
    def test_determine_verb(self):
        gesture1 = Gesture('Rock')
       
        gesture1.determine_verb('Scissors')
        self.assertEqual(gesture1.verb, 'crushes')
        gesture1.determine_verb('Lizard')
        self.assertEqual(gesture1.verb, 'crushes')
        gesture1.determine_verb('Spock')
        self.assertEqual(gesture1.verb, None)
        gesture1.determine_verb('Paper')
        self.assertEqual(gesture1.verb, None)
        
        
if __name__ == '__main__': 
    unittest.main()
