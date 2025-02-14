import pygame
import sys
import pickle
import tkinter
from tkinter import filedialog

from sprites.spritesheet import *
from sprites.dirt import *
from configs.screen_config import *
from map_translator import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.joystick.init()
        self.root = tkinter.Tk()
        self.root.withdraw()
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False

        self.screen = pygame.display.set_mode((SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        pygame.display.set_caption('Armistice')

        #   SPRITESHEETS

        self.dirt_spritesheet = SpriteSheet('img/terrain_spritesheets/dirt_spritesheet.png')
        self.dirt_spritesheet_dark = SpriteSheet('img/terrain_spritesheets/dirt_spritesheet_dark.png')
        self.active_tile_spritesheet = SpriteSheet('img/ui_images/active_tile.png')

        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.controller_input_string = f"Controller: {self.joystick.get_name()}"
        else:
            self.controller_input_string = "No Controller Detected"

        self.digging = False

    def new_game(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.dirt_group = pygame.sprite.LayeredUpdates()
        self.active_tile_group = pygame.sprite.LayeredUpdates()

        self.ground_map_layer_1 = ground_map_translator(self, 'data/map_layer_1.amf')
        self.ground_map_layer_2 = ground_map_translator(self, 'data/map_layer_2.amf')

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.playing = False
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            self.digging = True
        else:
            self.digging = False
        

    def update(self):
        self.all_sprites.update()

    def draw(self):
        #   self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)


        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def intro_screen(self):
        pass
