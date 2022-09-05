# CHILD CLASS


from player import Player
from time import sleep

class Human(Player):

    def __init__(self, name):
        super().__init__(name) 
        # self.name = name    
        # self.score = 0
        # self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        
    
    # Have to code to account for user error: if they type letters instead of numbers #     
    def human_gesture(self):
        while True:
            try:
                user_input = int(input("Make your move: "))
                if user_input not in range(5):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input, Try Again! ")
            
        self.selected_gesture = self.gesture_list[user_input]
        if user_input == 0:
            self.selected_gesture == "Rock"
        elif user_input == 1:
            self.selected_gesture == "Paper"
        elif user_input == 2:
            self.selected_gesture == "Scissors"
        elif user_input == 3:
            self.selected_gesture == "Lizard"
        elif user_input == 4:
            self.selected_gesture == "Spock"
        
        print(f'{self.name} chose {self.selected_gesture}')
        sleep(1)

       # When main_player is going to win the round, it double prints to terminal before telling me the winner 



            
    
           

        
       
        

        
        
            
       
       
       #❗ # WHEN WE LEFT: Thinking out how we would code out getting the geste (in human_gasture or get_gesture) and how that would affect the name that prints to terminal...❗

        
       
        
        
        
        
        

    

