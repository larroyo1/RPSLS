import unittest 
from cpu import Cpu 

class TestCpu(unittest.TestCase): 

    def test_instance(self): 
        computer = Cpu('Cpu')

        self.assertIsInstance(computer, Cpu)
        self.assertEqual(computer.name, 'Cpu')

    def test_choose_gesture(self): 
        computer = Cpu('Cpu')
        computer.choose_gesture()

        self.assertIn(computer.current_gesture, computer.gestures)

    def test_choose_character(self): 
        computer = Cpu('Cpu')
        computer.choose_character()

        self.assertIn(computer.name, computer.characters)

if __name__ == '__main__': 
    unittest.main()

