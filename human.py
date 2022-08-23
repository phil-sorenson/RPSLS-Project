from player import Player

class Human(Player):

    def __init__(self):
        name = self.get_name()
        super().__init__(name)

    def get_name(self):
        print('Name yourself')
        name = input()
        return name

    def get_gesture(self):
        print('Make your move')
        move = input() # will have to verify (move ,atches name on the list)
        
        return move
