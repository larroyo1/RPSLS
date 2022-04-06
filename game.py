from player import Player 
from cpu import Cpu

class Game:
    def __init__(self):
        self.player_one = Player('Sheldon')
        self.player_two = None

    def display_welcome(self):
        user_input = input('Welcome to RPSLS! Please enter 1 for single player or 2 for multiplayer.')
        
        if user_input == '1': 
            self.player_vs_cpu()
        elif user_input == '2': 
            self.player_vs_player()
        else: 
            print('Please input 1 or 2')
            self.display_welcome()
            
    def player_vs_player(self):
        self.player_two = Player('Penny')
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()

    def choose_winner(self, player_one_choice, player_two_choice):
        if player_one_choice == 'Rock' and player_two_choice in ['Paper', 'Spock']:
            print('Player two wins')
            self.player_two_score += 1 
        else: 
            print('Player one wins')
            self.player_two.score += 1 
        


    def player_vs_cpu(self):
        self.player_two = Cpu('Cpu')
    
    def run_game(self):
        pass

    def display_winner():
        pass
    