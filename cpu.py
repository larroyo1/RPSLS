from player import Player
import random
class Cpu(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.current_gesture = (random.choice(self.gestures))
    
    def choose_character(self):
        self.name = random.choice(self.characters)
        
