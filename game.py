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
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.choose_winner(self.player_one.current_gesture, self.player_two.current_gesture)

    def choose_winner(self, player_one_choice, player_two_choice):
            if player_one_choice == 'Rock' and player_two_choice in ['Paper', 'Spock']:
                print('Player two wins')
                self.player_two.score += 1 

            elif player_one_choice == 'Paper' and player_two_choice in ['Scissors','Lizard']:
                print('Player two wins')
                self.player_two.score += 1 

            elif player_one_choice == 'Scissors' and player_two_choice in ['Rock','Spock']:
                print('Player two wins')
                self.player_two.score += 1 

            elif player_one_choice == 'Lizard' and player_two_choice in ['Rock','Scissors']:
                print('Player two wins')
                self.player_two.score += 1 
            
            elif player_one_choice == 'Spock' and player_two_choice in ['Lizard','Paper']:
                print('Player two wins')
                self.player_two.score += 1
            
            elif player_one_choice == player_two_choice:
                print(f'Both players chose {player_one_choice}. DRAW.')

            else: 
                print('Player one wins')
                self.player_one.score += 1

    def player_vs_cpu(self):
        self.player_two = Cpu('Cpu')
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.choose_winner(self.player_one.current_gesture, self.player_two.current_gesture)

    def run_game(self):
        self.display_welcome()
        
        

    def display_winner():
        pass
    