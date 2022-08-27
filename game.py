import time
from ai import AI  # To delay the time between things that show on terminal
from human import Human



class Game:
    # will need gestutres & what beats what (MIGHT BE IN PLAYER or AI)
    # will need 1-2 players (human vs human or human vs AI)
    # game is over (best out of 3)
    
    def __init__(self):
        self.main_player = Human()
        self.player_two = Human() or AI() # <-- ???
        
        pass
       # QUESTION-- Not sure what to put in __init__ always 


    def start_game(self):
        self.game_rules()
        self.get_players()
        self.get_gesture()
        self.gesture_battle()
        self.best_of_three()
        # self.main_player = Human()
        # self.player_two = Human() or AI()    # Human or AI based on user input     QUESTION: How to give code out player_two being a human or ai based on user response??
        
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

    def convert_gestures_to_number(self, number):
        if (number == 0):
            return 'Rock'
        elif (number == 1):
            return 'Paper'
        elif (number == 2):
            return 'Scissor'
        elif (number == 3):
            return 'Lizard'
        elif (number == 4):
            return 'Spock'
        else:
            print('ERROR number, Try Again!')
       
        # Create ai class with player parent
        # Create score function
        # Call rounds (best of 3) --use inheritence (2 gestures, display winner/give points to,)
        # Function to announce winner
    def get_gesture(self):
        self.main_player_move = self.main_player.gesture()
        self.player_two_move = self.player_two.gesture()
        results = self.gesture_battle()
        return results
    
    
    def gesture_battle(self, move_one, move_two):
        
        if move_one == 'Rock':
            if move_two == 'scissors':
                print('Rock beats scissors, rock wins')
                return 'win'
            if move_two == 'lizard':
                print('rock crushes lizard, rock wins')
                return 'win'
            if move_two == 'rock':
                print('tie')
                return 'tie'
            if move_two == 'spock':
                print('you lose')
                return 'lose'
        if move_one == 'Paper':
            if move_two == 'scissors':
                print('scissors cuts paper, scissors wins')
                return 'lose'
            if move_two == 'lizard':
                print('lizard eats paper, lizard wins!')
                return 'lose'
            if move_two == 'rock':
                print("paper covers rock, paper wins!")
                return 'win'
         
       # another function (COULDNT THIS GO IN THE "Best_of_three" function?)
       # need to create 
       # while loop until someone hits two - announce winner
   
    def best_of_three(self):
        results = self.get_gesture()  # <--- QQQ: Would this need to call 'get_gesture' or 'gesture_battle'?
        if results == 'win':
            self.main_player.score = +1
        elif results == 'lose':
            self.player_two.score = +1
        return results

    def announce_winner(self):
        if self.main_player.score  >= 2:
            print(f'{self.main_player.name} has won!')
        elif self.player_two.score >= 2:
            print(f'{self.player_two.name} has won!')

        
        



        

            
        
    








