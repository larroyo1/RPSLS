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
            self.choose_winner(self.player_one.current_gesture, self.player_two.current_gesture)
            
    def choose_winner(self, player_one_choice, player_two_choice):
            if player_one_choice == 'Rock' and player_two_choice in ['Paper', 'Spock']:
                #self.display_round_outcome()
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 

            elif player_one_choice == 'Paper' and player_two_choice in ['Scissors','Lizard']:
                #self.display_round_outcome()
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 

            elif player_one_choice == 'Scissors' and player_two_choice in ['Rock','Spock']:
                #self.display_round_outcome()
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 

            elif player_one_choice == 'Lizard' and player_two_choice in ['Rock','Scissors']:
                #self.display_round_outcome()
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1 
            
            elif player_one_choice == 'Spock' and player_two_choice in ['Lizard','Paper']:
                #self.display_round_outcome()
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1
            
            elif player_one_choice == player_two_choice:
                print(f'Both players chose {player_one_choice}. DRAW.')

            else:
                #self.display_round_outcome() 
                print(f'{self.player_one.name} wins the round.')
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
            print(f'{self.player_one.name} chose {self.player_one.current_gesture} and {self.player_two.name} chose {self.player_two.current_gesture}')
            self.choose_winner(self.player_one.current_gesture, self.player_two.current_gesture)
            
            
    def display_score(self): 
        print(f'{self.player_one.name} has {self.player_one.score} points and {self.player_two.name} has {self.player_two.score} points.')
    #check this one out. it looks a little cleaner in the console. 
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
    #sorry, i couldn't help myself...
   # def display_round_outcome(self):
        # print(f'{self.player_one.name} chose {self.player_one.current_gesture} and {self.player_two.name} chose {self.player_two.current_gesture}.')
        # if self.player_one.current_gesture in ["Rock", "Scissors"] and self.player_two.current_gesture in ["Rock", "Scissors"]:
        #     print("Rock CRUSHES Scissors")
        #this is going to get long. 
        # Scissors cuts Paper 
        # Paper covers Rock 
        # Rock crushes Lizard 
        # Lizard poisons Spock
        # Spock smashes Scissors 
        # Scissors decapitates Lizard 
        # Lizard eats Paper 
        # Paper disproves Spock 
        # Spock vaporizes Rock 
        
    