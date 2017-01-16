# -*-coding: Utf-8 -*

"""
Connect Four game
Game in which 2 players take turns dropping discs in a board and try to
connect 4 of them.

Files : connect_four.py, datas.py, home_menu.py, side.py, board.py, player.py,
game.py

"""

import pygame
from pygame.locals import *

from datas import *
from home_menu import *
from side import *
from classes.game import Game
from classes.board import ConnectFourBoard
from classes.player import Player

pygame.init()

# Creating the window
screen = pygame.display.set_mode(window_size)
# window title
pygame.display.set_caption(window_title)
# window icon
icon = pygame.image.load(window_icon)
pygame.display.set_icon(icon)

# Creating home menu choices
arial_font = pygame.font.SysFont("Arial", 22)
# Render the menu items
label_one_player = arial_font.render("1 Player", 1, BLACK)
label_two_players = arial_font.render("2 Players (local)", 1, BLACK)
# label_online = arial_font.render("2 Players (online)", 1, BLACK)
menu_labels = (label_one_player, label_two_players)
menu_labels_pos = []


running = True
while running:

    # Load and display home image menu
    home = pygame.image.load(image_home).convert()
    screen.blit(home, (0, 0))
    # Displaying the home menu list
    menu_labels_pos = show_vertical_menu(screen, (570, 170), 50, *menu_labels)
    # Refresh view
    pygame.display.flip()

    # Initializing variables
    running_home = True
    running_game = True
    choice_menu = 0

    while running_home:
        # Speed loop limitation
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == QUIT:
                running = False
                running_game = False
                running_home = False
                choice_menu = 0

            if event.type == MOUSEMOTION:
                # Checking if the cursor is on one of the menu labels
                if mouse_on_menu_item(event, menu_labels_pos):
                    # Getting the label on which the mouse is on
                    label = mouse_on_menu_item(event, menu_labels_pos)
                    x = label['pos']['x']
                    y = label['pos']['y']
                    # And changing the label color into red
                    if str(label['label']) == str(label_one_player):
                        label_one_player = arial_font.render("1 Player", 1, RED)
                        screen.blit(label_one_player, (x, y))

                    elif str(label['label']) == str(label_two_players):
                        label_two_players = arial_font.render("2 Players (local)", 1, RED)
                        screen.blit(label_two_players, (x, y))

                    pygame.display.flip()
                # If not, reload and redisplay the default home menu
                else:
                    home = pygame.image.load(image_home).convert()
                    screen.blit(home, (0, 0))
                    menu_labels_pos = show_vertical_menu(screen, (570, 170), 50, *menu_labels)
                    # Refresh view
                    pygame.display.flip()

            if event.type == MOUSEBUTTONUP:
                # Checking if the cursor is on one of the menu labels
                if mouse_on_menu_item(event, menu_labels_pos):
                    # Getting the label on which the mouse is on
                    label = mouse_on_menu_item(event, menu_labels_pos)

                    if str(label['label']) == str(label_one_player):
                        choice_menu = 1
                        running_home = False

                    elif str(label['label']) == str(label_two_players):
                        choice_menu = 2
                        running_home = False



    if choice_menu != 0:
        # Create the players
        p1 = Player(p1_color)
        p2 = Player(p2_color)
        # Create the game
        game = Game(p1, p2, choice_menu)
        # We prepare the game
        game.prepare(screen)
        # Restart and home button
        position_restart = restart_button(screen)
        position_home = home_button(screen)



    while running_game:
        # Speed loop limitation
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == QUIT:
                running = False
                running_game = False
                running_home = False

            # Checking if the player is cliking on side buttons (restart, home)
            if event.type == MOUSEBUTTONUP and event.button == 1:
                # If the cursor is in the side zone (not the board game)
                if event.pos[0] > col_width * 7:
                    # If the player clicks on the restart button
                    if event.pos[0] >= position_restart[0] and \
                       event.pos[0] <= position_restart[0] + position_restart[2] and \
                       event.pos[1] >= position_restart[1] and \
                       event.pos[1] <= position_restart[1] + position_restart[3]:
                        # We restart the game
                        game.prepare(screen)
                        # Restart and home button
                        position_restart = restart_button(screen)
                        position_home = home_button(screen)

                    # If the player clicks on the home button
                    if event.pos[0] >= position_home[0] and \
                       event.pos[0] <= position_home[0] + position_home[2] and \
                       event.pos[1] >= position_home[1] and \
                       event.pos[1] <= position_home[1] + position_home[3]:
                        # We return at the home menu
                        running_game = False
                        running_home = True
                        break

            # The players are taking turns dropping discs
            game.run(screen, event)
