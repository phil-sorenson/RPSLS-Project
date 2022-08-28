
# CHILD CLASS

from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0
        
        

    def randomized_gesture(self):
        self.random_gesture = str(random.randint(0,4))  #❓If I were to call gesture list from Player class would it be; self.random_gesture = self.gesture(str(random.ranint(0,4)))❓
        gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"] # dont think this is needed since i could call "self.gesture" from Player class 
        sleep(1)
        print(f'{self.name} has picked {gesture_list[int(self.random_gesture)]}')
                        # Pretty sure "self.gesture" would work ⬆️ here as well                    


    # def get_name(self):
    #     print('Give your ai opponent a name!')
    #     name = input()
    #     return name