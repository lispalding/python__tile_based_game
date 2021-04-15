# MADE BY: Lisette Spalding
# FILE NAME: sprites.py
# PROJECT NAME: pygame__advanced_starter_template
# DATE CREATED: 03/05/2021
# DATE LAST MODIFIED: 04/13/2021
# PYTHON VER. USED: 3.8

##################### IMPORTS ######################
import pygame as pg
import random as r
from os import path

# Custom imports
from settings import *
##################### FINISHED #####################

################### GLOBAL VAR ####################
vec = pg.math.Vector2
##################### FINISHED #####################

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super(Player, self).__init__()

        ## Adding things to groups
        self.groups = game.allSprites

        self.game = game

        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PURPLE)

        # self.image = playerImage

        self.rect = self.image.get_rect()

        # Including vectors for movement and positioning
        self.velocity = vec(0, 0)
        self.position = vec(x, y) * TILE_SIZE

        ## Traditional Placement, speed, etc
        # # self.rect.center = (WIDTH/2, HEIGHT/2)
        # self.vx, self.vy = 0, 0
        # self.x = x * TILE_SIZE
        # self.y = y * TILE_SIZE
        # ## Placement FIN
        #
        # self.speedx = 0
        # self.speedy = 0

    def getKeys(self):
        """ To use: self.getKeys()
        This is the method that acquires the keys pressed and determines what to do """
        self.velocity = vec(0, 0)

        keys = pg.key.get_pressed() # Obtaining the key pressed
        # If the key pressed is the left arrow key OR the "a" key, then do this:
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.velocity.x = -PLAYER_SPEED

        # If the key pressed is the right arrow key OR the "d" key, then do this:
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.velocity.x = PLAYER_SPEED

        # If the key pressed is the up arrow key OR the "w" key, then do this:
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.velocity.y = -PLAYER_SPEED

        # If the key pressed is the down arrow key  or the "s" key, do this:
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.velocity.y = PLAYER_SPEED

        # If the x velocity does not equal 0 and the y velocity does not equal zero, do this:
        if self.velocity.x != 0 and self.velocity.y != 0:
            self.velocity *= 0.7071

    def collideWithWalls(self, dir):
        """ To use: self.collideWithWalls(dir)
        This is the method that checks to see if the player has collided with a wall, and how to deal with it. """
        if dir == "x":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.velocity.x > 0:
                    self.position.x = hits[0].rect.left - self.rect.width
                if self.velocity.x < 0:
                    self.position.x = hits[0].rect.right

                self.velocity.x = 0
                self.rect.x = self.position.x
        if dir == "y":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.velocity.y > 0:
                    self.position.y = hits[0].rect.top - self.rect.height
                if self.velocity.y < 0:
                    self.position.y = hits[0].rect.bottom

                self.velocity.y = 0
                self.rect.y = self.position.y

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

        self.position += self.velocity * self.game.dt

        # Setting up wall collision
        self.rect.x = self.position.x
        self.collideWithWalls("x")

        self.rect.y = self.position.y
        self.collideWithWalls("y")

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