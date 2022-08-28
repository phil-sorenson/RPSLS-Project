from player import Player

class Human(Player):

    def __init__(self):
        super().__init__()
        print('Name Yourself')
        self.name = input()
        print(f'Welcome {self.name} to RPSLS!')

    # def get_name(self):
    #     print('Name yourself')
    #     name = input()
    #     return name

    def choose_gesture(self):
        print('Make your move')
        move = self.gesture[0,4] # will have to verify (move matches name on the list)
        return move


# Question: Will i need to put points function in the player class? 