# -*-coding: Utf-8 -*

"""This module contains functions related to the home menu."""

import pygame
from pygame.locals import *


def show_vertical_menu(screen, pos, vertical_spacing, *labels):
    """Displays the menu on screen.

    Returns a dictionary that contains the menu items and their positions.

    Args:
        screen (Surface): surface where to display the menu
        pos (tuple): position of the menu
        vertical_spacing (int): vertical spacing between the items in pixels
        *labels (tuple): labels that represents the menu items

    """

    x = pos[0]
    y = pos[1]
    positions = []

    for label in labels:
        screen.blit(label, (x, y))
        positions.append({'label' : label, 'pos' : {'x' : x, 'y' : y} })
        y += vertical_spacing

    return positions


def mouse_on_menu_item(event, labels):
    """Returns the menu item on which the cursor is on, None otherwise.

    Args:
        event (Event): Mouse event to check for the cursor's position
        labels (dict): Contains the menu items and their positions

    """

    for label in labels:
        x = label['pos']['x']
        y = label['pos']['y']
        label_width = label['label'].get_width()
        label_height = label['label'].get_height()

        if event.pos[0] >= x and event.pos[0] <= x + label_width and \
           event.pos[1] >= y and event.pos[1] <= y + label_height:

            return label

    return None
