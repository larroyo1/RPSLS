from player import Player 
from cpu import Cpu
import time

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
            self.display_score()

    def choose_winner(self, player_one_choice, player_two_choice):
            if player_one_choice == 'Rock' and player_two_choice in ['Paper', 'Spock']:
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 

            elif player_one_choice == 'Paper' and player_two_choice in ['Scissors','Lizard']:
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 

            elif player_one_choice == 'Scissors' and player_two_choice in ['Rock','Spock']:
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 

            elif player_one_choice == 'Lizard' and player_two_choice in ['Rock','Scissors']:
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 
            
            elif player_one_choice == 'Spock' and player_two_choice in ['Lizard','Paper']:
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1
            
            elif player_one_choice == player_two_choice:
                print(f'Both players chose {player_one_choice}. DRAW.')

            else: 
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

    def player_vs_cpu(self):
        self.player_two = Cpu('Cpu')
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            time.sleep(1.5)
            print(f'{self.player_one.name} chose {self.player_one.current_gesture} and {self.player_two.name} chose {self.player_two.current_gesture}')
            time.sleep(1.5)
            self.choose_winner(self.player_one.current_gesture, self.player_two.current_gesture)
            time.sleep(1.5)
            self.display_score()
            time.sleep(1.5)

    def display_score(self): 
        print(f'{self.player_one.name} has {self.player_one.score} points and {self.player_two.name} has {self.player_two.score} points.')

    def run_game(self):
        self.display_welcome()
        self.display_winner()
        
        

    def display_winner(self):
        if self.player_one.score > self.player_two.score: 
            print(f'{self.player_one.name} wins the game!')
        else: 
            print(f'{self.player_two.name} wins the game!')
    