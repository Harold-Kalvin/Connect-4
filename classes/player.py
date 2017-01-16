# -*-coding: Utf-8 -*

"""This module contains the class 'Player'."""

class Player:

    """Class representing a Player."""

    def __init__(self, color):
        """Constructor of the class ConnectFourBoard."""
        self.color = color
        self.victory = 0
        self.name = "Player"


    def string_wins(self):
        """Returns the player's name and his number of wins in a string."""
        if self.victory <= 1:
            player = "{} : {} win".format(self.name.upper(), self.victory)
        else:
            player = "{} : {} wins".format(self.name.upper(), self.victory)
        return player
