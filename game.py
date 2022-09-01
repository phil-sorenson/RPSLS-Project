from time import sleep      # To delay time between lines in terminal
from ai import AI  
from human import Human


       # Create score function ✅
        # Call rounds (best of 3) --use inheritence (2 gestures, display winner/give points to,)
        # Function to announce winner ✅

class Game:
    
    def __init__(self):
        self.main_player = Human(input("Please enter your name: "))
        self.player_two = " "  
        pass
       


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
        print("")
        print('Each match will be the best of 3 games!\nUse the number keys to enter your selection.')
        sleep(1)
        print("Choose 0 for Rock.\nChoose 1 for Paper.\nChoose 2 for Scissors..\nChoose 3 for Lizard.\nChoose 4 for Spock.")
        sleep(1)
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
        sleep(1)
        print("")
        
        
    def get_opponent (self):
        print('Would you like to play against a human or ai? ')
        self.player_two = input()
        checked_players = 0
        while checked_players == 0:     # Edited opponent to be self.player_two so it calls from the AI() or Human() classes
            if self.player_two == 'human':
                print('human opponent')
                # Does🔻below🔻have to be an if conditional or while loop? in order to make self.player_two an AI or Human (if checked players==1 self.player_two = AI or Human)
                checked_players = 1
                self.player_two = Human("Player Two") # ⬅️ Will the way I identified player_two there name, work and do you need a break or return❓❓
                return self.player_two
            elif self.player_two == 'ai':
                print('ai opponent')
                checked_players = 1
                self.player_two = AI("Computer")
                return self.player_two
            else:
                print('You didn\'t type in human or ai, try again!')
                self.player_two = input()
        pass
                
                   

    
    # ❓❓ Do i even need a get_gesture function or can i just use the AI and Human classes to do that and just call to it from the gesture_battle❓❓
    
    #self.main_player.human_gesture()
    # if self.main_player.selevted_gesture == "Rock"
      
   

    def get_gesture(self):
        self.main_player.human_gesture()
        # print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')                                                   

        if self.player_two == AI():
            self.player_two.ai_gesture()
            # print(f"{self.player_two.name} chose {self.player_two.selected_gesture}") 
        elif self.player_two == Human():
            self.player_two.human_gesture()
            # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
        results = self.gesture_battle()
        return results
    # ❗Have to add a way for the player_two to be a human in get_gesture as well❗
    
    def gesture_battle(self): 

        if self.main_player.selected_gesture == 0:
            print(f'{self.main_player.name} has selected Rock')
            if self.player_two.selected_gesture == 0:
                print('tie')
                return 'tie'
            elif self.player_two.selected_gesture == 1:
                print(f'Paper covers Rock, {self.player_two.name} wins! ')
                return 'lose'
            elif self.player_two.selected_gesture == 2:
                print(f'Rock crushes scissors, {self.main_player.name} wins! ')
                return 'win'
            elif self.player_two.selected_gesture == 3:
                print(f'Rock crushes Lizard, {self.main_player.name} wins! ')
                return 'win'
            elif self.player_two.selected_gesture == 4:
                print(f'Spock vaporizes Rock, {self.player_two.name} wins! ')
                return 'lose'

        if self.main_player.selected_gesture == 1:
            if self.player_two.selected_gesture == 0:
                print(f'paper covers rock, {self.main_player.name} wins!')
                return 'win'
            elif move_two == 1:
                print('Tie')
                return 'tie'
            elif move_two == 2:
                print('Scissors cut paper, scissors win!')
                return 'lose'
            elif move_two == 3:
                print('lizard eats paper, lizard wins!')
                return 'lose'
            elif move_two == 4:
                print('Paper disproves Spock, Paper wins!')
                return 'win'
       
        if move_one == 2:
            if move_two == 0:
                print('Rock crushes scissors, Rock wins')
                return 'lose'
            elif move_two == 1:
                print("Scissors, cut paper, Scissors win!")
                return 'win'
            elif move_two == 2:
                print('Tie')
                return 'tie'
            elif move_two == 3:
                print('Scissors decapitate Lizard, Scissors win!')
                return 'win'
            elif move_two == 4:
                print('Spock smashes scissors, Spock wins!')
                return 'lose'

        if move_one == 3:
            if move_two == 0:
                print("Rock Crushes Lizard, Rock Wins!")
                return 'lose'
            elif move_two == 1:
                print('Lizard eats Paper, Lizard Wins!')
                return 'win'
            elif move_two == 2:
                print('scissors decapitates Lizard, scissors wins')
                return 'lose'
            elif move_two == 3:
                print('Tie')
                return 'tie'
            elif move_two == 4:
                print('Lizard poisons Spock, Lizard Wins!')
                return 'win'

        if move_one == 4:
            if move_two == 0:
                print("Spock vaporizes Rock, Spock Wins!")
                return 'win'
            elif move_two == 1:
                print('Paper disproves Spock, Paper wins!')
                return 'lose'        
            if move_two == 2:
                print('Spock smashes scissors, Spock Wins!')
                return 'wins'
            elif move_two == 3:
                print('lizard poisons Spock, lizard wins!')
                return 'lose'
            elif move_two == 4:
                print('Tie!')
                return 'Tie'

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
        sleep(1)
        input("Do you want to play again? y/n")
        if input == 'y':
            self.start_game()
        else:
            print("Thanks for Playing! ")
        
        

        
        


        

            
        
    








