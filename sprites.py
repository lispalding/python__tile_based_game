# MADE BY: Lisette Spalding
# FILE NAME: sprites.py
# PROJECT NAME: pygame__advanced_starter_template
# DATE CREATED: 03/05/2021
# DATE LAST MODIFIED: 03/05/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import *
from settings import *
################### FINISHED ###################

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super(Player, self).__init__()

        ## Adding things to groups
        self.groups = game.allSprites

        self.game = game

        self.image = pg.Surface((32, 32))
        self.image.fill(PURPLE)

        # self.image = playerImage

        self.rect = self.image.get_rect()

        ## Placement
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        self.x = x
        self.y = y
        ## Placement FIN

        self.speedx = 0
        self.speedy = 0

        self.keypressed = False

    def togglePressed(self):
        self.keypressed = False

    def move(self, dx= 0, dy = 0):
        self.x += dx
        self.y += dy

    def update(self):
        """ To use: self.update()
        This is the function that will update the movement of the player character. """
        ##### !! Basic Movement !! #####
        # self.speedx = 0
        # self.speedy = 0

        # Cheking the Keystate
        keystate = pg.key.get_pressed()

        ## Custom movement:
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE

        ########## .!. MOUSE CLICK AND DRAG
        if mouseBttnHeld:
            self.rect.center = (mousex, mousey)
        ########## .!. MOUSE CLICK AND DRAG FIN

        ######### !!!! .. MOUSE FINISHED .. !!!! ##########

        ##### !!!! .. SCREEN BINDING .. !!!! #####
        # We are binding the player to the screen area
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        ##### !!!! .. BINDING FINISH .. !!!! #####

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # Setting up the groups
        self.groups = game.allSprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)

        # Initializing the Game variable
        self.game = game
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))

        self.image.fill(GREEN) # Filling the walls with green

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE