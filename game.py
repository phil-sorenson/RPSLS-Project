import time
from human import Human



class Game:
    # will need gestutres & what beats what (MIGHT BE IN PLAYER or AI)
    # will need 1-2 players (human vs human or human vs AI)
    # game is over (best out of 3)
    def __init__(self):
        print('Started init')   # Edit later


    def start_game(self):
        self.game_rules()
        self.get_players()
        self.main_player = Human()
        self.player_one_move = self.main_player.get_gesture()
        # Create ai class with player parent
        # Create score function
        # Call rounds (best of 3) --use inheritence (2 gestures, display winner/give points to,)
        # Function to announce winner


        

    def game_rules(self):
        print('Welcome to Rock, Paper, Scissor, Lizard, Spock!')
        time.sleep(1)
        print('each match will be the best of 3 games!\nUse the number keys to enter your selection.')
        time.sleep(1)
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper')

    def get_players (self):
        print('Would you like to play against a human or ai? ')
        opponent = input()
        checked_players = 0
        while checked_players == 0:
            if opponent == 'human':
                print('human opponent')
                checked_players = 1
                break
            elif opponent == 'ai':
                print('ai opponent')
                checked_players = 1
                break
            else:
                print('You didn\'t type in human or ai, try again!')
                opponent = input()
            
        
    








