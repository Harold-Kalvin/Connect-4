# -*-coding: Utf-8 -*

"""This module contains the class 'ConnectFourBoard'."""

import operator

import pygame
from pygame.locals import *

from datas import *

class ConnectFourBoard:

    """Class representing a connect four board with its squares."""

    def __init__(self, cols, rows):
        """Constructor of the class ConnectFourBoard."""
        self.cols = cols
        self.rows = rows
        self.board = []
        for i in range(cols):
            col = []
            for j in range(rows):
                col.append(None)
            self.board.append(col)
        self.square_img = pygame.image.load(image_square).convert_alpha()
        self.square_px = self.square_img.get_width() # size of a square
        self.height = self.square_img.get_height() * self.rows
        self.width = self.square_px * self.cols
        self.disc_rad = int(self.square_px / 2.5) # disc's size
        self.current_color = None
        self.current_square = None
        self.row_of_four = [] # will contain the 4 winner discs' positions


    def show_board(self, screen):
        """This method draws the board using pygame's 'draw methods'.

        This method is called everytime a visual change must be done.

        Args:
            screen (Surface): surface where to draw the board

        """

        # Placing the squares
        x = 0
        for col in self.board:
            y = 0
            for row in col:
                screen.blit(self.square_img, (x, y))
                y += int(self.square_px)
            x += int(self.square_px)


    def _next_square(self, col):
        """Returns the next free square (index) in a specified column.

        Args:
            col (int): board's column where to search for the next free square

        """

        slot = 0
        for i, value in enumerate(self.board[col]):
            if value is None:
                slot = i
                break
        return slot


    def add_disc(self, col, screen, disc_color):
        """This method adds a new disc in the board and displays it visually.

        Args:
            col (int): column index where to drop the disc
            screen (Surface): surface where to draw the new disc
            disc_color (tuple): color of the new disc

        """

        # Creating the disc's x position (First board column)
        x = int(self.square_px / 2)
        x_col = int(self.square_px * col)
        # Initialize the disc's y position
        y = 0
        y_next = (self.height - self.square_px / 2) - \
                 (self.square_px * self._next_square(col))

        if None in self.board[col]:
            # We update some useful attributes
            self.current_color = disc_color
            self.current_square = (col, self._next_square(col))
            # We replace the 'None value' of the board with the 'color value'
            self.board[col][self._next_square(col)] = disc_color

            # Animation of the falling disc
            while y <= y_next:
                pygame.draw.circle(screen, bg_color, [x + x_col, y - self.disc_rad], self.disc_rad, 0)
                pygame.draw.circle(screen, disc_color, [x + x_col, y], self.disc_rad, 0)
                self.show_board(screen)
                pygame.display.flip()
                y += 4 # falling speed


    def _is_same_color(self, x, y):
        """Returns True if the color of the current disc matches the color of
        another disc which the position is given by the arguments x and y.

        Args:
            x (int): x position of the compared disc
            y (int): y position of the compared disc

        """

        # x and y stays within the board range
        if not x < self.cols or not y < self.rows or not x >= 0 or not y >= 0:
            return False

        # We check if the color matches
        if self.current_color == self.board[x][y]:
            return True

        return False


    def verify_victory(self):
        """Returns True if there's a winner, False otherwise.

        The method checks if the current disc is in row of 4 discs of the same
        color.

        """

        # Checking if a move has already been made (to check for a winner)
        if self.current_square:

            # Intializing x and y (position of the current disc)
            x = self.current_square[0]
            y = self.current_square[1]

            lines = {
                'horizontal' : {
                    'left' : { 'x' : (x, operator.sub, 1), 'y' : (y, operator.add, 0) },
                    'right' : { 'x' : (x, operator.add, 1), 'y' : (y, operator.add, 0) }
                },
                'vertical' : {
                    'down' : { 'x' : (x, operator.add, 0), 'y' : (y, operator.sub, 1) }
                },
                'diagonal_desc' : {
                    'up-left' : { 'x' : (x, operator.sub, 1), 'y' : (y, operator.add, 1) },
                    'down-right' : { 'x' : (x, operator.add, 1), 'y' : (y, operator.sub, 1) }
                },
                'diagonal_asc' : {
                    'up-right' : { 'x' : (x, operator.add, 1), 'y' : (y, operator.add, 1) },
                    'down-left' : { 'x' : (x, operator.sub, 1), 'y' : (y, operator.sub, 1) }
                }
            }

            # For each lines (horizontal, vertical etc.)
            for key_line, line in lines.items():
                self.row_of_four.append((x, y))
                win = 1

                # For each direction in lines (left, right etc.)
                for key_direction, direction in line.items():

                    # Initializing x and y next values
                    # For example for left ('y' doesn't change) : x - 1, y
                    operator_x = direction['x'][1]
                    operator_y = direction['y'][1]
                    next_x = operator_x(direction['x'][0], direction['x'][2])
                    next_y = operator_y(direction['y'][0], direction['y'][2])
                    # If there is at least one disc of the same color
                    # next to the current disc
                    if self._is_same_color(next_x, next_y):
                        # We test it 4 times in the same direction
                        for i in range(1, 4):

                            if win == 4:
                                break

                            # Only x needs to change
                            if key_line == 'horizontal':
                                next_x = direction['x'][1](direction['x'][0], i)

                            # Only y needs to change
                            if key_line == 'vertical':
                                next_y = direction['y'][1](direction['y'][0], i)

                            # Both x and y needs to change
                            if key_line in ['diagonal_desc', 'diagonal_asc']:
                                next_x = direction['x'][1](direction['x'][0], i)
                                next_y = direction['y'][1](direction['y'][0], i)

                            if self._is_same_color(next_x, next_y):
                                win += 1
                                self.row_of_four.append((next_x, next_y))
                            else:
                                break

                if win >= 4:
                    return True
                else:
                    self.row_of_four = []

        return False


    def highlight_winner(self, screen, color):
        """Highlights the victor's row of 4.

        Args:
            color (tuple): Color in which the row is highlighted

        """

        for i, pos in enumerate(self.row_of_four):
            x = int(pos[0] * self.square_px + self.square_px / 2)
            y = int((self.height - pos[1] * self.square_px) - self.square_px / 2)
            pygame.draw.circle(screen, color, [x, y], int(self.disc_rad / 1.5), 0)

        pygame.display.flip()
