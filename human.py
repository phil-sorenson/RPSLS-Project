# CHILD CLASS



from player import Player
from time import sleep
class Human(Player):

    def __init__(self, name):
        super().__init__(name) 
        # self.name = name    
        # self.score = 0
        # self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        
    
           
    def human_gesture(self):
        user_input = int(input("Please make your move: "))
        self.selected_gesture = self.gesture_list[user_input]
        if user_input > 5:
            print('Invalid number...Please try again! (0-4): ')
            self.human_gesture()
        elif user_input < 0:
            print('Invalid number...Please try again! (0-4): ')
            self.human_gesture()
        if user_input == 0:
            self.selected_gesture = "Rock"
        elif user_input == 1:
            self.selected_gesture = "Paper"
        elif user_input == 2:
            self.selected_gesture = "Scissors"
        elif user_input == 3:
            self.selected_gesture = "Lizard"
        elif user_input == 4:
            self.selected_gesture = "Spock"

        



            
    
           

        
       
        

        
        
            
       
       
       #❗ # WHEN WE LEFT: Thinking out how we would code out getting the geste (in human_gasture or get_gesture) and how that would affect the name that prints to terminal...❗

        
       
        
        
        
        
        

    

