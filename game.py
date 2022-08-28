from time import sleep # To delay time between lines in terminal
from ai import AI  
from human import Human
from player import Player


class Game:
    # will need gestutres & what beats what (MIGHT BE IN PLAYER or AI)
    # will need 1-2 players (human vs human or human vs AI)✅
    # game is over (best out of 3)
    
    def __init__(self):
        self.main_player = Human(Player)
        self.player_two = Human(Player) or AI(Player) # <-- ???
        
        pass
       # QUESTION-- Not sure what to put in __init__ always 


    def start_game(self):
        self.game_rules()
        self.get_opponent()
        self.get_gesture()
        self.gesture_battle()
        self.best_of_three()
    
        # self.main_player = Human()
        # self.player_two = Human() or AI()    # Human or AI based on user input     QUESTION❓: How to give code out player_two being a human or ai based on user response??
        
    def game_rules(self):
        print('Welcome to Rock, Paper, Scissor, Lizard, Spock!')
        sleep(1)
        print('Each match will be the best of 3 games!\nUse the number keys to enter your selection.')
        sleep(1)
        # print('1.Rock\n2.Paper\n3.Scissor\n4.Lizard\n5.Spock') <---❓ NOT SURE ABOUT HOW TO GO ABOUT THIS 
        # time.sleep(1)
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')

        
    def get_opponent (self):
        print('Would you like to play against a human or ai? ')
        self.player_two = input()
        checked_players = 0
        while checked_players == 0:     # Edited opponent to be self.player_two so it calls from the AI() or Human() classes
            if self.player_two == 'human':
                print('human opponent')
                checked_players = 1
                self.player_two = Human()
                break
            elif self.player_two == 'ai':
                print('ai opponent')
                checked_players = 1
                self.player_two = AI()   # <---❓IS THIS HOW TO RUN THESE OPPONENTS AS HUMAN OR AI❓
                break
            else:
                print('You didn\'t type in human or ai, try again!')
                self.player_two = input()

    def convert_gestures_to_number(self, number):
        print('Choose 0 for Rock.\nChoose 1 for Paper.\nChoose 2 for Scissor.\nChoose 3 for Lizard.\nChoose 4 for Spock.')
        if (number == 0):
            return 'Rock'
        elif (number == 1):
            return 'Paper'           #❓ DONT NEED SINCE ITS BEING CALLED FROM A LIST ❓❓
        elif (number == 2):
            return 'Scissor'
        elif (number == 3):
            return 'Lizard'
        elif (number == 4):
            return 'Spock'
        else:
            print('ERROR number, Try Again!')
       
        # Create ai class with player parent
        # Create score function ✅
        # Call rounds (best of 3) --use inheritence (2 gestures, display winner/give points to,)
        # Function to announce winner ✅
    def get_gesture(self):
        self.main_player_move = self.main_player.gesture[0,4]   #❓<--- Not sure if [0,4] needed to be added ❓
        self.player_two_move = self.player_two.gesture[0,4]
        results = self.gesture_battle()
        return results
    
    
    def gesture_battle(self, move_one, move_two): 
        
        if move_one == 0:
            if move_two == 2:
                print('Rock crushes scissors, rock wins')
                return 'win'
            if move_two == 'lizard':
                print('rock crushes lizard, rock wins')
                return 'win'
            if move_two == 'rock':
                print('tie')
                return 'tie'
            if move_two == 'spock':
                print('Spock vaporizes Rock, Spock Wins!')
                return 'lose'
        
        if move_one == 'Paper':
            if move_two == 'scissors':
                print('scissors cut paper, scissors win!')
                return 'lose'
            if move_two == 'lizard':
                print('lizard eats paper, lizard wins!')
                return 'lose'
            if move_two == 'rock':
                print("paper covers rock, paper wins!")
                return 'win'
            if move_two == 'spock':
                print('Paper disproves Spock, Paper wins!')
                return 'win'
            if move_two == 'paper':
                print('Tie')
                return

        if move_one == 'Scissors':
            if move_two == 'rock':
                print('Rock crushes scissors, Rock wins')
                return 'lose'
            if move_two == 'lizard':
                print('Scissors decapitate Lizard, Scissors win!')
                return 'win'
            if move_two == 'paper':
                print("Scissors, cut paper, Scissors win!")
                return 'win'
            if move_two == 'spock':
                print('Spock smashes scissors, Spock wins!')
                return 'lose'
            if move_two == 'scissors':
                print('Tie')
                return 'tie'
            
        if move_one == 'Lizard':
            if move_two == 'scissors':
                print('scissors decapitates Lizard, scissors wins')
                return 'lose'
            if move_two == 'lizard':
                print('Tie')
                return 'tie'
            if move_two == 'rock':
                print("Rock Crushes Lizard, Rock Wins!")
                return 'lose'
            if move_two == 'spock':
                print('Lizard poisons Spock, Lizard Wins!')
                return 'win'
            if move_two == 'paper':
                print('Lizard eats Paper, Lizard Wins!')
                return 'win'

        if move_one == 'Spock':
            if move_two == 'scissors':
                print('Spock smashes scissors, Spock Wins!')
                return 'wins'
            if move_two == 'lizard':
                print('lizard poisons Spock, lizard wins!')
                return 'lose'
            if move_two == 'rock':
                print("Spock vaporizes Rock, Spock Wins!")
                return 'win'
            if move_two == 'spock':
                print('Tie!')
                return 'Tie'
            if move_two == 'paper':
                print('Paper disproves Spock, Paper wins!')
                return 'lose'
         
       # ❗NEED TO CODE A WAY FOR PLAYER_TWO TO GET POINTS AS WELL❗
       # while loop until someone hits two - announce winner
   
    def best_of_three(self):
        results = self.get_gesture()  # <--- QQQ❓: Would this need to call 'get_gesture' or 'gesture_battle'?
        if results == 'win':
            self.main_player.score = +1
        elif results == 'lose':
            self.player_two.score = +1
            return results
        while self.main_player.score < 2 or self.player_two.score < 2:
            self.get_gesture()
            if self.main_player.score >= 2:
                self.announce_winner()
                break
            if self.player_two.score >= 2:
                self.announce_winner()
                break
            



    def announce_winner(self):
        if self.main_player.score  >= 2:
            print(f'{self.main_player.name} has won!')
        elif self.player_two.score >= 2:
            print(f'{self.player_two.name} has won!')

        
        


        

            
        
    








