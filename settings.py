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

################ MATH VARIABLE #################
vec = pg.math.Vector2
################### FINISHED ###################


########## BASIC VARIABLES ###########
WIDTH = 1024
HEIGHT = 668
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
######### PLAYER SETTINGS ##########
PLAYER_HEALTH = 100

PLAYER_SPEED = 300
PLAYER_ROTATION_SPEED = 250

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

PLAYER_IMAGE = "manBlue_gun.png"

PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

BARREL_OFFSET = vec(30, 10)
############ FINISHED #############

######### BULLET SETTINGS ##########
BULLET_IMAGE = "bullet.png"

BULLET_SPEED = 500
BULLET_LIFESPAN = 1000

FIRING_RATE = 150

KICKBACK = 200
GUN_SPREAD = 5

BULLET_DAMAGE = 10
############ FINISHED #############
############## FINISHED ###############

############ NPC VARIABLES #############
########## WALL SETTINGS ##########
WALL_IMAGE = "tileGreen_39.png"
############ FINISHED #############

######### ZOMBIE SETTINGS #########
ZOMBIE_IMAGE = "zoimbie1_hold.png"

ZOMBIE_SPEEDS = [150, 100, 75, 125, 150]

ZOMBIE_HIT_RECT = pg.Rect(0, 0, 30, 30)

ZOMBIE_HEALTH = 100
ZOMBITE = 10
ZOMBITE_KNOCKBACK = 20

AVOID_RADIUS = 50
############ FINISHED #############
############## FINISHED ###############

###### SPECIAL EFFECTS VARIABLES ######
########### GUN EFFECTS ###########
MUZZLE_FLASHES = ["whitePuff15.png", "whitePuff16.png", "whitePuff17.png", "whitePuff18.png"]

FLASH_DURATION = 40
############ FINISHED #############
############## FINISHED ###############

################ LAYERS ################
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
ZOMBIE_LAYER = 2
EFFECTS_LAYER = 4
############## FINISHED ###############

######### FOLDER SETUP #########
gameFolder = path.dirname(__file__) # General folder set-up

# Map folders
mapsFolder = path.join(gameFolder, "maps")

textMapsFolder = path.join(mapsFolder, "textfile_maps")
firstTiledMapFolder = path.join(mapsFolder, "map1_tiled")

## Basic image folders
imageFolder = path.join(gameFolder, "images")
spritesheetImgFolder = path.join(imageFolder, "Spritesheet")
pngImgFolder = path.join(imageFolder, "PNG")

## Character image folders
# Player image folder
manBlueImageFolder = path.join(pngImgFolder, "Man Blue")

# Zombie image folder
zombieImageFolder = path.join(pngImgFolder, "Zombie 1")

## Wall image folder
wallImageFolder = path.join(pngImgFolder, "Tiles")

## Basic sound folder
soundFolder = path.join(gameFolder, "sounds")

## Basic text data folder
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
YELLOW = (252, 240, 3)
BROWN = (106, 55, 5)

LIGHT_GREY = (100, 100, 100)
YELLOW_GREEN = (182, 219, 18)
LIGHT_BLUE = (100, 162, 209)
PALE_YELLOW = (245, 233, 154)

# Shortcut colors
BG_COLOR = BROWN
############# FIN #############