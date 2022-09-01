# CHILD CLASS



from player import Player
from time import sleep
class Human(Player):

    def __init__(self,name):
        super().__init__()     
        self.name = name 
        # self.score = 0
        # self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        
    
    # storing the selected gesture:
    def human_gesture(self):
        if user_input == 0:
            self.selected_gesture = "Rock"
            return "Rock"
        elif user_input == 1:
            self.selected_gesture = "Paper"
            return "Paper"
        elif user_input == 2:
            self.selected_gesture = "Scissors"
            return "scissors"
        elif user_input == 3:
            self.selected_gesture = "Lizard"
            return "Lizard"
        elif user_input == 4:
            self.selected_gesture = "Spock"
            return "Lizard"
        else:
            input("Invalid entry, Try again: ")
        
        user_input = int(input("Please make your move: "))
        self.selected_gesture = self.gesture_list[user_input]
        
        print(f"{self.name} chose {self.selected_gesture}")
        
            
       
       
       #❗ # WHEN WE LEFT: Thinking out how we would code out getting the geste (in human_gasture or get_gesture) and how that would affect the name that prints to terminal...❗

        
       
        
        
        
        
        

    

