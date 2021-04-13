# MADE BY: Lisette Spalding
# FILE NAME: sprites.py
# PROJECT NAME: pygame__advanced_starter_template
# DATE CREATED: 03/05/2021
# DATE LAST MODIFIED: 04/13/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import path

# Custom imports
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
        self.vx, self.vy = 0, 0
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        ## Placement FIN

        self.speedx = 0
        self.speedy = 0

    def getKeys(self):
        """ To use: self.getKeys()
        This is the method that acquires the keys pressed and determines what to do """
        self.vx, self.vy = 0, 0

        keys = pg.key.get_pressed() # Obtaining the key pressed
        # If the key pressed  is the left arrow key OR the "a" key, then do this:
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collideWithWalls(self, dir):
        """ To use: self.collideWithWalls(dir)
        This is the method that checks to see if the player has collided with a wall, and how to deal with it. """
        if dir == "x":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == "y":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        """ To use: self.update()
        This is the method that will update the movement of the player character. """
        ##### !! Basic Movement !! #####
        # self.speedx = 0
        # self.speedy = 0

        # Cheking the Keystate
        keystate = pg.key.get_pressed()

        ## Custom movement:
        self.getKeys()

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        # Setting up wall collision
        self.rect.x = self.x
        self.collideWithWalls("x")
        self.rect.y = self.y
        self.collideWithWalls("y")


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