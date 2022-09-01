# CHILD CLASS



from player import Player
from time import sleep
class Human(Player):

    def __init__(self, name):
        super().__init__()     
        self.name = name
        # self.score = 0
        # self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        
    
    # storing the selected gesture:         # ←← Whats best way to go about this❓ selected_gesture = " " or return " "
    def human_gesture(self):
        user_input = int(input("Please make your move: "))
        if user_input == 0:
            return "Rock"
        elif user_input == 1:
            return "Paper"
        elif user_input == 2:
            return "Scissors"
        elif user_input == 3:
            return "Lizard"
        elif user_input == 4:
            return "Spock"
        else:
            input("Invalid entry, Try again: ")
            self.human_gesture()
        self.selected_gesture = self.gesture_list[user_input]
        
       
        

        
        
            
       
       
       #❗ # WHEN WE LEFT: Thinking out how we would code out getting the geste (in human_gasture or get_gesture) and how that would affect the name that prints to terminal...❗

        
       
        
        
        
        
        

    

