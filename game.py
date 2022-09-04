from time import sleep      # To delay time between lines in terminal
from ai import AI  
from human import Human


# TODO:  1. Edit the invalid number & word response in Human 'user_input'-- create a Error for if player types in a string instead of numbers
       # 2. Opponent name prints twice to terminal after an error was made--need to fix
       # 3. Find a way to print gesture selection to terminal immediately after "Please Make Move:" instead of all at once 
       # 4. Find a way to delay inbetween each gesture rule in game_rules

      

class Game:
    
    def __init__(self):
        self.main_player = Human("Main Player")
        self.player_two = "" 
        pass
       


    def start_game(self):
        self.game_rules()
        self.get_opponent()
        # self.get_gesture()
        self.gesture_battle()
        self.best_of_three()
    
    
        # self.main_player = Human()
        # self.player_two = Human() or AI()    # Human or AI based on user input     QUESTION❓: How to give code out player_two being a human or ai based on user response??
        
    def game_rules(self):
        print('')
        print('Welcome to Rock, Paper, Scissor, Lizard, Spock!')
        print('===================================================')
        sleep(1)
        print('Each match will be the best of 3 games!\nUse the number keys to enter your selection.')
        print("     ")
        print("")
        sleep(1)
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
        print(" ")
        sleep(1)
        print("Choose 0 for Rock.\nChoose 1 for Paper.\nChoose 2 for Scissors.\nChoose 3 for Lizard.\nChoose 4 for Spock.")
        sleep(1)
        print("")
        
        
    def get_opponent (self):
        print('Would you like to play against a human or ai? ')
        self.input_opponent = input()
        checked_players = 0
        while checked_players == 0:    
            if self.input_opponent == 'human':
                self.player_two = Human("Player 2")
                print(f'{self.player_two.name} is your opponent')
                print('')
                checked_players = 1
               
            elif self.input_opponent == 'ai':
                self.player_two = AI("Computer")
                print(f'{self.player_two.name} is your opponent')
                print('')
                checked_players = 1
               
            else:
                print('You didn\'t type in human or ai, try again!')
                self.get_opponent()  
                # prints opponent name twice after mistake was made--need to fix    
        pass
                
                                                    
                
                
                
                   

    
   
      
   

    # def get_gesture(self):
    #     self.main_player.human_gesture()
    #     print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')                                                   
    #     if self.player_two == AI("Computer"):
    #         self.player_two.ai_gesture()
    #         print(f'{self.player_two.name} has picked {self.player_two.gesture_list[int(self.player_two.selected_gesture)]}')
    #     elif self.player_two == Human("Player 2"):
    #         self.player_two.human_gesture()
    #         print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
    #     # results = self.gesture_battle()
    #     # return results
    
    
   

        
    
    def gesture_battle(self):
        self.round_outcome = ""        # self.main_player_wins = self.main_player.score += 1
        
        self.main_player.human_gesture()
        if self.input_opponent == 'human':
            self.player_two.human_gesture()  
        elif self.input_opponent == 'ai': 
            self.player_two.ai_gesture()

        
        
        

        if self.main_player.selected_gesture == self.player_two.selected_gesture:
            print('It\'s A Tie, Play again!')
            sleep(2)
            print()
            print()
            self.gesture_battle()

        if self.main_player.selected_gesture == "Rock":
            print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            if self.player_two.selected_gesture == "Paper":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins! ')
                print('')
                self.round_outcome == 'lose'
                sleep(1)
            elif self.player_two.selected_gesture == "Scissors":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'
            elif self.player_two.selected_gesture == "Lizard":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'
            elif self.player_two.selected_gesture == "Spock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'


        if self.main_player.selected_gesture == "Paper":
            print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'   
            elif self.player_two.selected_gesture == "Scissors":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'
            elif self.player_two.selected_gesture == "Lizard":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'
            elif self.player_two.selected_gesture == "Spock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'
                

        if self.main_player.selected_gesture == "Scissor":
            print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'    
            elif self.player_two.selected_gesture == "Paper":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'
            elif self.player_two.selected_gesture == "Lizard":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'
            elif self.player_two.selected_gesture == "Spock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'


        if self.main_player.selected_gesture == "Lizard":
            print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'    
            elif self.player_two.selected_gesture == "Paper":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'
            elif self.player_two.selected_gesture == "Scissor":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'
            elif self.player_two.selected_gesture == "Spock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'


        if self.main_player.selected_gesture == "Spock":
            print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'    
            elif self.player_two.selected_gesture == "Paper":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'
            elif self.player_two.selected_gesture == "Scissors":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.round_outcome == 'win'
            elif self.player_two.selected_gesture == "Lizard":
                print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.round_outcome == 'lose'
        self.best_of_three()

       # while loop until someone hits two - announce winner
   
    def best_of_three(self):
                                        # <--- QQQ❓: Would this need to call 'get_gesture' or 'gesture_battle'?
        if self.round_outcome == 'win':
            self.main_player.score += 1
        elif self.round_outcome == 'lose':
            self.player_two.score += 1
        if self.main_player.score < 2 or self.player_two.score < 2:
            self.gesture_battle()
        if self.main_player.score >= 2:
                self.announce_winner()
        elif self.player_two.score >= 2:
                self.announce_winner()
                


    def announce_winner(self):
        if self.main_player.score  >= 2:
            print(f'{self.main_player.name} has won the game!')
        elif self.player_two.score >= 2:
            print(f'{self.player_two.name} has won the game!')
        sleep(1)
        input("Do you want to play again? y/n ")
        if input == 'y':
            self.start_game()
        else:
            print("Thanks for Playing! ")
        
        

        
        


        

            
        
    








