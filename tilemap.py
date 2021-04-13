# MADE BY: Lisette Spalding
# FILE NAME: tilemap.py
# PROJECT NAME: pygame__advanced_starter_template
# DATE CREATED: 04/13/2021
# DATE LAST MODIFIED: 04/13/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import path

# Custom imports
from settings import *
################### FINISHED ###################

class Map:
    """ To use: Map()
     This is the map class, it will load the maps necessary for the game. """
    def __init__(self, filename):
        self.data = []

        with open(filename, "rt") as f:
            for line in f:
                self.data.append(line.strip())

        # Obtaining the tile width & height
        self.tileWidth = len(self.data[0])
        self.tileHeight = len(self.data)

        # Obtaining the general width & height
        self.width = self.tileWidth * TILE_SIZE
        self.height = self.tileHeight * TILE_SIZE

class Camera:
    """ To use: Camera()
    This is the Camera class, which will bind the metaphorical camera to the player. """
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)

        self.width = width
        self.height = height

    def apply(self, entity):
        """ To use: self.apply(entity)
        This method that keeps the entity that the camera is bound to in the center of the screen. """
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        """ To use: self.update(target)
        This is the method that keeps the map/camera updated as the player moves. """
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # Limiting scrolling to map size
        x = min(0, x) # Left limit
        y = min(0, y) # Top limit
        x = max(-(self.width - WIDTH), x) # Right limit
        y = max(-(self.height - HEIGHT), y) # Bottom limit

        # Adjusting the camera rectangle
        self.camera = pg.Rect(x, y, self.width, self.height)