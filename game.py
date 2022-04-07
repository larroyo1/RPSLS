from player import Player 
from cpu import Cpu
import time

class Game:
    def __init__(self):
        self.player_one = Player("Player 1")
        self.player_two = Player("Player 2") 
        self.game_mode = None     

    def display_welcome(self):
        self.game_mode = input('Welcome to RPSLS! Please enter 1 for single player or 2 for multiplayer.')

    def player_vs_player(self):
        self.player_one.choose_character()
        self.player_two.characters.remove(self.player_one.name)
        self.player_two.choose_character()

        while self.player_one.score < 2 and self.player_two.score < 2:
            self.display_round_info()
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.current_gesture.name} and {self.player_two.name} chose {self.player_two.current_gesture.name}')
            self.determine_winner()
    
    def determine_winner(self):
        self.player_one.current_gesture.determine_verb(self.player_two.current_gesture.name)
        self.player_two.current_gesture.determine_verb(self.player_one.current_gesture.name)

        if self.player_one.current_gesture.name == self.player_two.current_gesture.name:
            print(f'Both players chose {self.player_one.current_gesture.name}. DRAW.')
        elif self.player_one.current_gesture.verb == None:
            print(f'{self.player_two.current_gesture.name} {self.player_two.current_gesture.verb} {self.player_one.current_gesture.name}!')
            print(f'{self.player_two.name} wins the round!')
            self.player_two.score += 1
        elif self.player_two.current_gesture.verb == None:
            print(f'{self.player_one.current_gesture.name} {self.player_one.current_gesture.verb} {self.player_two.current_gesture.name}!')
            print(f'{self.player_one.name} wins the round!')
            self.player_one.score += 1
    
    def player_vs_cpu(self):
        self.player_one.choose_character()
        self.player_two = Cpu('Player 2')
        self.player_two.characters.remove(self.player_one.name)
        self.player_two.choose_character()

        while self.player_one.score < 2 and self.player_two.score < 2:
            self.display_round_info()
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()            
            print(f'{self.player_one.name} chose {self.player_one.current_gesture.name} and {self.player_two.name} chose {self.player_two.current_gesture.name}')
            self.determine_winner()
            
    def display_score(self): 
        print(f'{self.player_one.name} has {self.player_one.score} points and {self.player_two.name} has {self.player_two.score} points.')
     
    def display_round_info(self):
        round_number = 1
        print(f'Round {round_number}')
        print(f'{self.player_one.name}: {self.player_one.score} pts VS {self.player_two.name}: {self.player_two.score} pts.')
        round_number += 1

    def run_game(self):
        self.display_welcome()

        if self.game_mode == '1':
            self.player_vs_cpu()
        elif self.game_mode == '2':
            self.player_vs_player()
        else:
            print("That is not a valid response.")
            self.display_welcome()
            
        self.display_winner()
        
    def display_winner(self):
        if self.player_one.score > self.player_two.score: 
            print(f'{self.player_one.name} wins the game!')
        else: 
            print(f'{self.player_two.name} wins the game!')
        
    