from player import Player

class Human(Player):

    def __init__(self):
        name = self.get_name()
        super().__init__(name)

    def get_name(self):
        print('Name yourself')
        name = input()
        return name

    def gesture(self):
        print('Make your move')
        move = input() # will have to verify (move matches name on the list)
        return move


# Question: Will i need to put points function in the player class? 