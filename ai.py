
# CHILD CLASS


from unicodedata import name
from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):         
        super().__init__()
        self.name = name
        # self.score = 0
        # self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"] 
        
        

    def ai_gesture(self):
        self.selected_gesture = str(random.randint(0,4)) 
        sleep(1)
        # print(f'{self.name} has picked {self.gesture_list[int(self.selected_gesture)]}')
                                  

