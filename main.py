# (5 points): As a developer, I want to make at least 10 commits with descriptive messages. ✅
# (15 points): As a developer, I want to find a way to properly incorporate inheritance into my game. ✅ (Player class == is PARENT class and human & AI are == Child classes)
# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.
# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).
# NOTE: Do not use a Gesture class until you have reached MVP for all user stories and been checked off by an instructor!
# (10 points): As a player, I want the correct player to win a given round based on the choices made by each player. See Framework document for game rules!
# (10 points): As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.
# (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.

# Rock crushes Scissors Scissors cuts Paper Paper covers Rock Rock crushes Lizard Lizard poisons Spock Spock smashes Scissors Scissors decapitates Lizard Lizard eats Paper
# Create seperate classes for each gesture in order to simplify battle (in each class identify what it loses to, wins to and ties with)

from game import Game
# if __name__ == '__main__': # NOT SURE WHAT THIS IS--JUST COPIED FROM WALKTHROUGH
run_game = Game()
run_game.start_game()



# ❓How to use a integer(#) as gesture choice instead of user having to type out 'gestures name'
# ❓How to go about "human" class's and "ai" class's __init__ function -- Inheritance needed? -- self.name = input() ??
        # How to do name as an Input() along with inheritance
# ❓❓(Game class) Depending on respose (Human or AI opponent), run it properly (aka randomly or manually) and how to go about the Name
        # When calling Human() & AI() in Game class do I need to put Player in the parameters since its inheritance?❓
# ❓(AI & Human class) If I were to call gesture list from Player class instead of just putting the list in AI & Human class, would it be; self.random_gesture = self.gesture(str(random.ranint(0,4)))❓
# ❓(Game Class) Announce the winner for each round as opposed to just "rock wins", etc...
# ❓Is it easier to do win_lose_pairs ??
# ❓Where/How should I access 'Player' in the game class?
# ❓




