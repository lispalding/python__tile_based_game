# MADE BY: Lisette Spalding
# ART WORK CREDIT: "Kenney.nl" @ "www.kenney.nl"
# FILE NAME: sprites.py
# PROJECT NAME: python__tile_based_game
# DATE CREATED: 03/05/2021
# DATE LAST MODIFIED: 05/11/2021
# PYTHON VER. USED: 3.x

##################### IMPORTS ######################
import pygame as pg
import random as r
from os import path

# Custom imports
from settings import *
from tilemap import collideHitRect
##################### FINISHED #####################

################### GLOBAL VAR #####################
vec = pg.math.Vector2
##################### FINISHED #####################

################ GLOBAL FUNCTIONS ##################
def collideWithWalls(sprite, group, dir):
    """ To use: self.collideWithWalls(dir)
    This is the method that checks to see if the player has collided with a wall, and how to deal with it. """
    if dir == "x":
        hits = pg.sprite.spritecollide(sprite, group, False, collideHitRect)
        if hits:
            if sprite.velocity.x > 0:
                sprite.position.x = hits[0].rect.left - sprite.hitRect.width / 2
            if sprite.velocity.x < 0:
                sprite.position.x = hits[0].rect.right + sprite.hitRect.width / 2

            sprite.velocity.x = 0
            sprite.hitRect.centerx = sprite.position.x

    if dir == "y":
        hits = pg.sprite.spritecollide(sprite, group, False, collideHitRect)
        if hits:
            if sprite.velocity.y > 0:
                sprite.position.y = hits[0].rect.top - sprite.hitRect.height / 2
            if sprite.velocity.y < 0:
                sprite.position.y = hits[0].rect.bottom + sprite.hitRect.height / 2

            sprite.velocity.y = 0
            sprite.hitRect.centery = sprite.position.y
##################### FINISHED #####################

##################### CLASSES ######################
class Spritesheet():
    """ To use: Spritesheet()
        This class will parse and load spritesheets. """
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def getImage(self, x, y, width, height):
        """ To use: getImage(x, y, width, height)
        This method obtains an image, grabbing it from the larger spritesheet. """
        # Grabbing an image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))

        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super(Player, self).__init__()

        ## Adding things to groups
        self.groups = game.allSprites

        self.game = game

        # self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        # self.image.fill(PURPLE)

        self.image = self.game.playerImage

        # self.image = self.game.spritesheet.getImage(263, 132, 49, 43)
        # self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.hitRect = PLAYER_HIT_RECT
        self.hitRect.center = self.rect.center

        # Including vectors for movement and positioning
        self.velocity = vec(0, 0)
        self.position = vec(x, y) * TILE_SIZE

        self.rotation = 0 # This variable tracks how much (how far) the player has rotated. Allowing the sprite to face in more than one direction.

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
        self.rotationSpeed = 0
        self.velocity = vec(0, 0)

        keys = pg.key.get_pressed() # Obtaining the key pressed
        # If the key pressed is the left arrow key OR the "a" key, then do this:
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rotationSpeed = PLAYER_ROTATION_SPEED

        # If the key pressed is the right arrow key OR the "d" key, then do this:
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rotationSpeed = -PLAYER_ROTATION_SPEED

        # If the key pressed is the up arrow key OR the "w" key, then do this:
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.velocity = vec(PLAYER_SPEED, 0).rotate(-self.rotation)

        # If the key pressed is the down arrow key  or the "s" key, do this:
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.velocity = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rotation)

        # SOLVING DIAGONAL ISSUE: !! NO LONGER NEEDED !!
        # If the x velocity does not equal zero and the y velocity does not equal zero, do this:
        # if self.velocity.x != 0 and self.velocity.y != 0:
        #     self.velocity *= 0.7071

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

        self.rotation = (self.rotation + self.rotationSpeed * self.game.dt) % 360

        # Taking care of image rotation:
        self.image = pg.transform.rotate(self.game.playerImage, self.rotation)

        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Rotation FIN

        self.position += self.velocity * self.game.dt

        # Setting up wall collision
        self.hitRect.centerx = self.position.x
        collideWithWalls(self, self.game.walls, "x")

        self.hitRect.centery = self.position.y
        collideWithWalls(self, self.game.walls, "y")

        self.rect.center = self.hitRect.center

class Zombie(pg.sprite.Sprite):
    """ To use: Zombie()
    This class will create an NPC (In this case, a zombie). """
    def __init__(self, game, x, y):
        # Setting up the groups
        self.groups = game.allSprites, game.zombieGroup
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game

        self.image = game.zombieImage
        self.rect = self.image.get_rect() # Setting up the rectangle
        self.hitRect = ZOMBIE_HIT_RECT.copy()
        self.hitRect.center = self.rect.center

        # Setting up movement:
        self.position = vec(x, y) * TILE_SIZE
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)

        # Setting up spawn point(s):
        self.rect.center = self.position

        # Setting up the zombie movement
        self.rotation = 0

    def update(self):
        """ To use: self.update()
        This is the method that will update the movement of the player character. """
        self.rotation = (self.game.player.position - self.position).angle_to(vec(1, 0))

        self.image = pg.transform.rotate(self.game.zombieImage, self.rotation) # Rotating the mob image as it faces player
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # Movement:
        self.acceleration = vec(ZOMBIE_SPEED, 0).rotate(-self.rotation)
        self.acceleration += self.velocity * -1
        self.velocity += self.acceleration * self.game.dt
        self.position += self.velocity * self.game.dt + 0.5 * self.acceleration * self.game.dt ** 2

        # Resetting rectangle
        self.hitRect.centerx = self.position.x
        collideWithWalls(self, self.game.walls, "x")
        self.hitRect.centery = self.position.y
        collideWithWalls(self, self.game.walls, "y")

        self.rect.center = self.hitRect.center


class Wall(pg.sprite.Sprite):
    """ To use: Wall()
    This class creates walls in the game-- Dependent on the maps."""
    def __init__(self, game, x, y):
        # Setting up the groups
        self.groups = game.allSprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)

        # Initializing the Game variable
        self.game = game
        self.image = game.wallImage

        # self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        # self.image.fill(GREEN) # Filling the walls with green

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
##################### FINISHED #####################