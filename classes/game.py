# -*-coding: Utf-8 -*

"""This module contains the class 'Game'."""

import random

import pygame
from pygame.locals import *

from datas import *
from side import *
from classes.board import ConnectFourBoard
from classes.player import Player

class Game:

    """Class representing a game of connect four."""

    def __init__(self, player1, player2, mode):
        """Constructor of the class Game."""
        self.board = None
        self.mode = mode
        self.player1 = player1
        self.player2 = player2
        if mode == 1:
            self.player1.name = 'Player 1'
            self.player2.name = 'Computer'
        elif mode == 2:
            self.player1.name = 'Player 1'
            self.player2.name = 'Player 2'


    def prepare(self, screen):
        """Displays the interface (board, side informations...).

        Args:
            screen (Surface): surface where to draw the board

        """

        # We prepare the game
        screen.fill(bg_color)
        self.board = ConnectFourBoard(7, 6)
        self.board.show_board(screen)
        pygame.display.flip()
        # Displaying some useful informations on the side of the window
        show_turn(screen, self.player1)
        show_wins(screen, self.player1, self.player2)


    def _take_turns(self, screen, col):
        """Adds a disc in the board and looks for a winner each turn.

        Args:
            screen (Surface): surface where to drop the new disc
            col (int): column index where to drop the new disc

        """

        # We alternate colors before adding the discs
        if self.board.current_color != self.player1.color:
            self.board.add_disc(col, screen, self.player1.color)
            show_turn(screen, self.player2)
        else:
            self.board.add_disc(col, screen, self.player2.color)
            show_turn(screen, self.player1)

        # We check if the match has a winner after a turn
        if self.board.verify_victory():

            if self.board.current_color == self.player1.color:
                self.player1.victory += 1
                show_wins(screen, self.player1, self.player2)
                show_win_sentence(screen, self.player1)
            else:
                self.player2.victory += 1
                show_wins(screen, self.player1, self.player2)
                show_win_sentence(screen, self.player2)

            self.board.highlight_winner(screen, WHITE)


    def _player_turn(self, screen, event):
        """The player chooses a column by clicking on the interface.

        Args:
            screen (Surface): surface where to drop the new disc
            event (Event): Mouse event to check for the cursor's position

        """

        if event.type == MOUSEBUTTONUP and event.button == 1:
            # If the player clicks on the board
            if event.pos[0] < col_width:
                self._take_turns(screen, 0)
            elif event.pos[0] > col_width and event.pos[0] < col_width * 2:
                self._take_turns(screen, 1)
            elif event.pos[0] > col_width * 2 and event.pos[0] < col_width * 3:
                self._take_turns(screen, 2)
            elif event.pos[0] > col_width * 3 and event.pos[0] < col_width * 4:
                self._take_turns(screen, 3)
            elif event.pos[0] > col_width * 4 and event.pos[0] < col_width * 5:
                self._take_turns(screen, 4)
            elif event.pos[0] > col_width * 5 and event.pos[0] < col_width * 6:
                self._take_turns(screen, 5)
            elif event.pos[0] > col_width * 6 and event.pos[0] < col_width * 7:
                self._take_turns(screen, 6)



    def _computer_turn(self, screen):
        """The computer chooses a column.

        Args:
            screen (Surface): surface where to drop the new disc

        """
        # The computer chooses a column randomly (for now)
        cols = [0, 1, 2, 3, 4, 5, 6]
        choice = random.choice(cols)

        if None in self.board.board[choice]:
            self._take_turns(screen, choice)
        else:
            self._computer_turn(screen)



    def run(self, screen, event):
        """Runs the right game mode (1 player, 2 players...).

        Args:
            screen (Surface): surface where to drop the new disc
            event (Event): Mouse event to check for the cursor's position

        """

        # If there is no winner yet, then the match goes on
        if not self.board.verify_victory():

            # One player mode, the player is against the computer
            if self.mode == 1:
                if self.player1.color != self.board.current_color:
                    self._player_turn(screen, event)
                else:
                    self._computer_turn(screen)

            # Two players mode, two players against each other
            if self.mode == 2:
                self._player_turn(screen, event)
