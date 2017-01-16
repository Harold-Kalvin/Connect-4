# -*-coding: Utf-8 -*

"""This module contains functions related to the side informations in game."""

import pygame
from pygame.locals import *

from datas import *


def show_turn(screen, player):
    """Displays the player that must play the turn.

    Args:
        screen (Surface): surface where to display the player that must play
        player (Player): displayed player

    """

    # Preparing the text
    arial_font = pygame.font.SysFont("Arial", 22)
    text = "{}'s turn".format(player.name.upper())
    # We hide the text that has been previously drawn
    hide_label = pygame.draw.rect(screen, bg_color, [615, 20, 190, 26], 0)
    # We write the new text
    label_player = arial_font.render(text, 1, WHITE)
    screen.blit(label_player, (615, 20))
    # Draw the disc with the right color
    current_disc = pygame.draw.circle(screen, player.color, [680, 100], 32, 0)
    # Refresh the view
    pygame.display.flip()


def show_wins(screen, player1, player2):
    """Displays the number of wins of each player.

    Args:
        screen (Surface): surface where to display the number of wins
        player1 (Player): Player 1
        player2 (Player): Player 2

    """

    arial_font = pygame.font.SysFont("Arial", 22)
    # We hide the text that has been previously drawn
    hide_label = pygame.draw.rect(screen, bg_color, [610, 150, 190, 55], 0)
    # We write the new text
    p1_wins = arial_font.render(player1.string_wins(), 1, WHITE)
    p2_wins = arial_font.render(player2.string_wins(), 1, WHITE)
    screen.blit(p1_wins, (610, 150))
    screen.blit(p2_wins, (610, 180))
    pygame.display.flip()


def show_win_sentence(screen, player):
    """Displays a text that shows which player won the game.

    Args:
        screen (Surface): surface where to display the text
        player (Player): player that won the game

    """

    arial_font = pygame.font.SysFont("Arial", 22)
    # We hide the text that has been previously drawn
    pygame.draw.rect(screen, bg_color, [600, 20, 190, 115], 0)
    # We write the new text
    winner = "We have a winner !"
    player = player.name.upper()
    label_winner = arial_font.render(winner, 1, WHITE)
    label_player = arial_font.render(player, 1, WHITE)
    screen.blit(label_winner, (600, 40))
    screen.blit(label_player, (600, 75))
    pygame.display.flip()


def restart_button(screen):
    """Displays the 'restart' button.

    Args:
        screen (Surface): surface where to display the button

    """

    arial_font = pygame.font.SysFont("Arial", 22)
    # Create restart button
    pos = [600, 300, 160, 35]
    pygame.draw.rect(screen, BLUE, pos, 0)
    label = arial_font.render('RESTART GAME', 1, WHITE)

    screen.blit(label, (610, 305))
    pygame.display.flip()

    return pos


def home_button(screen):
    """Displays the 'return home' button.

    Args:
        screen (Surface): surface where to display the button

    """

    arial_font = pygame.font.SysFont("Arial", 22)
    # Create return home button
    pos = [600, 350, 160, 35]
    pygame.draw.rect(screen, BLUE, pos, 0)
    label = arial_font.render('RETURN HOME', 1, WHITE)

    screen.blit(label, (610, 355))
    pygame.display.flip()

    return pos
