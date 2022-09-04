
# CHILD CLASS



from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):         
        super().__init__(name)
        # self.name = name
        # self.score = 0
        # self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"] 
        
        
# Not sure whether to put "int" or "str" and where
    def ai_gesture(self):
        self.selected_gesture = str(random.choice(self.gesture_list))
        sleep(1)
        # print(f'{self.name} has picked {self.gesture_list[int(self.selected_gesture)]}')
        
        if self.selected_gesture == 0:
            self.selected_gesture == "Rock"
        elif self.selected_gesture == 1:
                self.selected_gesture == "Paper"
        elif self.selected_gesture == 2:
                self.selected_gesture == "Scissors"
        elif self.selected_gesture == 3:
                self.selected_gesture == "Lizard"
        elif self.selected_gesture == 4:
                self.selected_gesture == "Spock" 
                             

