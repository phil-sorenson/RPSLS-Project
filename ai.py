from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name
        
    # def get_name(self):
    #     print('Give your ai opponent a name!')
    #     name = input()
    #     return name

    def randomized_gesture(self):
        self.random_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        sleep(1)
        print(f'{self.name} has picked {gesture_list[int(self.random_gesture)]}')
                             

