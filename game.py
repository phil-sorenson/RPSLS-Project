from time import sleep      # To delay time between lines in terminal
from ai import AI  
from human import Human


# TODO:  1. Edit the invalid number & word response in Human 'user_input'-- create a Error for if player types in a string instead of numbers✅
       # 2. Opponent name prints twice to terminal after an error was made--need to fix 
       # 3. Find a way to print gesture selection to terminal immediately after "Please Make Move:" instead of all at once✅ 
       # 4. Find a way to delay inbetween each gesture rule in game_rules✅
       # 5. Finish Scoring function! 

# QUESTIONS: ▫️ If you "run" python file and the terminal is stuck on an "input" line how do you get out of it and stop running? 
      

class Game:
    
    def __init__(self):
        self.main_player = Human("Main Player")
        self.player_two = "" 
        pass
       


    def start_game(self):
        # self.game_rules()
        self.get_opponent()
        self.gesture_battle()
        self.best_of_three()
        # self.announce_winner()
        # self.get_winner()
    
    
        # self.main_player = Human()
        # self.player_two = Human() or AI()    # Human or AI based on user input     QUESTION❓: How to give code out player_two being a human or ai based on user response??
        
    def game_rules(self):
        print('')
        print('Welcome to Rock, Paper, Scissor, Lizard, Spock!')
        print('===================================================')
        sleep(1)
        print('Each match will be the best of 3 games!')
        print("")
        sleep(.5)
        print('Use the number keys to enter your selection.')
        sleep(.5)
        print('Choose 0 for Rock')
        sleep(.5)
        print('Choose 1 for Paper.')
        sleep(.5)
        print('Choose 2 for Scissors.')
        sleep(.5)
        print('Choose 3 for Lizard.')
        sleep(.5)
        print('Choose 4 for Spock.')
        sleep(1)
        print("")
        print('Rock crushes Scissors')
        sleep(.5)
        print('Scissors cuts Paper')
        sleep(.5)
        print('Paper covers Rock')
        sleep(.5)
        print('Rock crushes Lizard')
        sleep(.5)
        print('Lizard poisons Spock')
        sleep(.5)
        print('Spock smashes Scissors')
        sleep(.5)
        print('Scissors decapitates Lizard')
        sleep(.5)
        print('Lizard eats Paper')
        sleep(.5)
        print('Paper disproves Spock')
        sleep(.5)
        print('Spock vaporizes Rock')
        print(" ")
        sleep(1)
        
        
        
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
                self.input_opponent = input()  
                # prints opponent name twice after mistake was made--need to fix    
        
    
        
    # def get_winner(self):
    #     self.round_outcome = ''
    #     
            
   

        
    
    def gesture_battle(self):
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
            if self.player_two.selected_gesture == "Paper":
                print()
                sleep(.5)
                print(f'{self.player_two.name} wins! ')
                print('')
                self.main_player.round_outcome = 'lose'
                pass
                sleep(.5)
            elif self.player_two.selected_gesture == "Scissors":
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'
                pass
                sleep(.5)
            elif self.player_two.selected_gesture == "Lizard":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'
            elif self.player_two.selected_gesture == "Spock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'


        if self.main_player.selected_gesture == "Paper":
            # print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'   
            elif self.player_two.selected_gesture == "Scissors":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'
            elif self.player_two.selected_gesture == "Lizard":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'
            elif self.player_two.selected_gesture == "Spock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'
                

        if self.main_player.selected_gesture == "Scissors":
            # print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'    
            elif self.player_two.selected_gesture == "Paper":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'
            elif self.player_two.selected_gesture == "Lizard":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'
            elif self.player_two.selected_gesture == "Spock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'


        if self.main_player.selected_gesture == "Lizard":
            # print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'    
            elif self.player_two.selected_gesture == "Paper":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'
            elif self.player_two.selected_gesture == "Scissors":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'
            elif self.player_two.selected_gesture == "Spock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'


        if self.main_player.selected_gesture == "Spock":
            # print(f'{self.main_player.name} chose {self.main_player.selected_gesture}')
            sleep(1)
            if self.player_two.selected_gesture == "Rock":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'    
            elif self.player_two.selected_gesture == "Paper":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'
            elif self.player_two.selected_gesture == "Scissors":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.main_player.name} wins!')
                print('')
                self.main_player.round_outcome = 'win'
            elif self.player_two.selected_gesture == "Lizard":
                # print(f'{self.player_two.name} chose {self.player_two.selected_gesture}')
                print()
                sleep(1)
                print(f'{self.player_two.name} wins!')
                print('')
                self.main_player.round_outcome = 'lose'

        
        if self.main_player.round_outcome == 'win':
            self.main_player.score += 1  
        elif self.main_player.round_outcome == 'lose':
            self.player_two.score += 1
         
       
       # while loop until someone hits two - announce winner
   
    def best_of_three(self):
# TODO: # Figure out why stystem bypasses the scoring points function after the first round points have been scored and given to winning player
        
        # if self.main_player.round_outcome == 'win':
        #     self.main_player.score += 1  
        # elif self.main_player.round_outcome == 'lose':
        #     self.player_two.score += 1

        while self.main_player.score <= 1 and self.player_two.score <= 1:
            self.gesture_battle()
        if self.main_player.score == 2:
            print(f'{self.main_player.name} has won the game! ')
            sleep(.5)
        elif self.player_two.score == 2:
            print(f'{self.player_two.name} has won the game! ')
            sleep(.5)
        play_again = input('Do you want to play again? y/n ')
        if play_again == 'y':
            self.start_game()
        else:
            print('Thanks For Playing! ')        


    # def announce_winner(self):
    #     if self.main_player.score  == 2:
    #         print(f'{self.main_player.name} has won the game!')
    #     elif self.player_two.score == 2:
    #         print(f'{self.player_two.name} has won the game!')
    #     sleep(1)
    #     input("Do you want to play again? y/n ")
    #     if input == 'y':
    #         self.start_game()
    #     else:
    #         print("Thanks for Playing! ")
        
        

        
        


        

            
        
    








