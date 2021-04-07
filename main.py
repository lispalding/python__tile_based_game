# MADE BY: Lisette Spalding
# FILE NAME: main.py
# PROJECT NAME: python__tile_based_game
# DATE CREATED: 04/07/2021
# DATE LAST MODIFIED: 04/07/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import *

# Custom Imports
from settings import *
from sprites import *
################### FINISHED ###################

################ MAIN GAME LOOP ################
####### Game class #######
class Game(object):
    """ To use: Game()
    This class runs the main game. """
    def __init__(self):
        self.running = True

        pg.init()  # Initializing Pygame Library
        pg.mixer.init()  # Sounds

        # Initializing display
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)

        # Initializing clock
        self.clock = pg.time.Clock()

        # Setting repeat variable
        pg.key.set_repeat(500, 100)

        self.loadData()

    def loadData(self):
        """ To use: self.loadData()
        This method creates data for maps. """
        self.mapData = []
        with open(path.join(mapsFolder, "map.txt"), "rt") as f:
            for line in f:
                self.mapData.append(line)

    def new(self):
        """ To use: self.new()
        This method creates a new game. """
        # Creating the sprite groups
        self.allSprites = pg.sprite.Group() # All sprites group
        self.playerGroup = pg.sprite.Group() # Player group

        self.walls = pg.sprite.Group() # The Walls group

        ## Creating the game objects
        self.player = Player(self, 10, 10)
        # Adding player to sprite groups
        self.allSprites.add(self.player)
        self.playerGroup.add(self.player)

        # Spawning walls
        for row, tiles in enumerate(self.mapData):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)

        # Start running game loop...
        self.run()

    def run(self):
        """ To use: self.run()
        This method runs the game. """
        ## Game loop
        self.playing = True

        while self.playing:
            self.clock.tick(FPS)

            # Processing input events
            self.events()

            # Processing updated variables
            self.update()

            # Creating the images on the screen
            self.draw()

    def events(self):
        """ To use: self.events()
        This method keeps track of the events that happen throughout running the game. """
        for event in pg.event.get():
            # Check for closing windows:
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False

                # Movement events:
                if event.key == pg.K_LEFT:
                    self.player.move(dx = -1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx = 1)
                if event.key == pg.K_UP:
                    self.player.move(dy = -1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy = 1)

    def update(self):
        """ To use: self.update()
        This method updates what is shown on the HUD. """
        self.allSprites.update()

    def drawGrid(self):
        """ To use: self.drawGrid()
        This method draws a grid on the screen. Useful for tile-based games. """
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, LIGHT_GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, LIGHT_GREY, (0, y), (WIDTH, y))

    def draw(self):
        """ To use: self.draw()
        This method draws the content on the screen. """
        self.screen.fill(BLACK)

        ## Customizing the draw() method for a tile-based game:
        self.drawGrid()
        ## FIN

        self.allSprites.draw(self.screen)

        ## This is the very last thing to happen during the draw:
        pg.display.flip()

    def showStartingScreen(self):
        """ To use: self.showStartingScreen()
        This method shows the starting screen. """
        pass

    def showGameOverScreen(self):
        """ To use: self.showGameOverScreen()
        This method shows the game over screen. """
        pass

####### Finished #######

g = Game() # Defining the game start

g.showStartingScreen() # Showing the starting screen for the new game

while g.running:
    g.new() # This kicks off the actual game loop
    g.showGameOverScreen()

# If the loop ever breaks this happens:
pg.quit()
################### FINISHED ###################