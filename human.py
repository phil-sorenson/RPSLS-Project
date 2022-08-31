# CHILD CLASS



from player import Player
from time import sleep
class Human(Player):

    def __init__(self,name):
        super().__init__()        # ❓ Question with name
        self.name = name
        self.score = 0
        self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        
    
    
    def human_gesture(self):
        print("Make Your Move!")
        self.human_move = input()
        

        sleep(1)
        # will have to verify (move matches name on the list)
        
        
        
        
        

    # def get_name(self):
    #     print('Name yourself')
    #     name = input()
    #     return name



# Question: Will i need to put points function in the player class? 