from player import Player
import random

class AI(Player):
    def __init__(self):
        name = self.get_name()
        super().__init__(name)

    def get_name(self):
        print('Give your ai opponent a name!')
        name = input()
        return name

    def get_gesture(self):
        self.gesture # get length (.len) of list and get random number within that length (self.gesture[random number]--return move)

