# MADE BY: Lisette Spalding
# ART WORK CREDIT: "Kenney.nl" @ "www.kenney.nl"
# FILE NAME: settings.py
# PROJECT NAME: python__tile_based_game
# DATE CREATED: 03/25/2021
# DATE LAST MODIFIED: 05/11/2021
# PYTHON VER. USED: 3.x

################### IMPORTS ####################
import pygame as pg
import random as r
from os import path
################### FINISHED ###################

########## BASIC VARIABLES ###########
WIDTH = 1024
HEIGHT = 768
FPS = 60

# Mouse button - Held?
mouseBttnHeld = False

# Title
title = "Python Tile Game"
############## FINISHED ##############

########## GAME VARIABLES ###########
TILE_SIZE = 64

GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

CHARACTERS_SPRITESHEET = "spritesheet_characters.png"
############## FINISHED ##############

########## PLAYER VARIABLES ###########
PLAYER_SPEED = 300
PLAYER_ROTATION_SPEED = 250

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

PLAYER_IMAGE = "manBlue_gun.png"

PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
############## FINISHED ###############

############ NPC VARIABLES #############
WALL_IMAGE = "tileGreen_39.png"
############## FINISHED ###############

######### FOLDER SETUP #########
gameFolder = path.dirname(__file__) # General folder set-up

# Map folder
mapsFolder = path.join(gameFolder, "maps")

## Individual maps folders
map1File = path.join(mapsFolder, "map.txt")

# Basic image folders
imageFolder = path.join(gameFolder, "images")
spritesheetImgFolder = path.join(imageFolder, "Spritesheet")
pngImgFolder = path.join(imageFolder, "PNG")

# Character image folders
manBlueImageFolder = path.join(pngImgFolder, "Man Blue")

# Basic sound folder
soundFolder = path.join(gameFolder, "sounds")

# Basic text data folder
textDataFolder = path.join(gameFolder, "text_data")
########### FINISHED ###########

###### COLORS  (R. G. B) ######
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Custom Colors
ORANGE = (242, 162, 41)
MINT = (63, 232, 159)
PURPLE = (182, 103, 224)
PINK = (224, 103, 139)
YELLOW = (245, 233, 154)

LIGHT_GREY = (100, 100, 100)
YELLOW_GREEN = (182, 219, 18)
LIGHT_BLUE = (100, 162, 209)

# Shortcut colors
BG_COLOR = BLACK
############# FIN #############