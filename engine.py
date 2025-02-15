import pygame
import sys
import pickle
import tkinter
from tkinter import filedialog

from sprites.spritesheet import *
from sprites.dirt import *
from configs.screen_config import *
from map_translator import *
from camera import *


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
        self.screen_buffer = pygame.Surface((SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.screen_buffer_rect = self.screen_buffer.get_rect(x=0, y=0)
        pygame.display.set_caption('Armistice')

        self.camera = Camera(self)


        #   SPRITESHEETS

        self.dirt_spritesheet = SpriteSheet('img/terrain_spritesheets/dirt_spritesheet.png')
        self.dirt_spritesheet_dark = SpriteSheet('img/terrain_spritesheets/dirt_spritesheet_dark.png')
        self.active_tile_spritesheet = SpriteSheet('img/ui_images/active_tile.png')
        self.trench_furnishings_spritesheet = SpriteSheet('img/object_spritesheets/trench_furnishings_spritesheet.png')

        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.controller_input_string = f"Controller: {self.joystick.get_name()}"
        else:
            self.controller_input_string = "No Controller Detected"

        self.digging = False

        self.camera_speed = 3
        self.zoom_level = 1

    def new_game(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.dirt_group = pygame.sprite.LayeredUpdates()
        self.active_tile_group = pygame.sprite.LayeredUpdates()
        self.bunks = pygame.sprite.LayeredUpdates()
        self.sandbags = pygame.sprite.LayeredUpdates()

        self.ground_map_layer_1 = ground_map_translator(self, 'data/map_layer_1.amf')
        self.ground_map_layer_2 = ground_map_translator(self, 'data/map_layer_2.amf')
        self.funiture_map = furniture_map_translator(self, 'data/furniture_map.amf')

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.playing = False
                self.running = False

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    if self.zoom_level < 2:
                        self.zoom_level += 0.02
                    else: 
                        self.zoom_level = 2
                if event.y < 0:
                    if self.zoom_level > 0.5:
                        self.zoom_level -= 0.02
                    else:
                        self.zoom_level = 0.5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            self.digging = True
        else:
            self.digging = False

        if keys[pygame.K_UP]:
            if self.zoom_level < 2:
                self.zoom_level += 0.02
            else: 
                self.zoom_level = 2
        if keys[pygame.K_DOWN]:
            if self.zoom_level > 0.5:
                self.zoom_level -= 0.02
            else:
                self.zoom_level = 0.5

    def update(self):
        
        self.all_sprites.update()
        self.camera.update()


        if self.zoom_level > 2:
            self.zoom_level = 2
        elif self.zoom_level < 0.5:
            self.zoom_level = 0.5

        self.camera_speed = self.camera_speed*self.zoom_level
        if self.camera_speed >= 6:
            self.camera_speed = 6

    def draw(self):
        self.screen.fill(BLACK)
        self.screen_buffer.fill(BLACK)
        self.all_sprites.draw(self.screen_buffer)
        
        
        #   LOGIC FOR CAMERA ZOOM HERE - SELF.SCREEN_BUFFER.TRANSFORM OR SOMETHING
        
        zoomed = pygame.transform.scale_by(self.screen_buffer, self.zoom_level)
        zoomed_rect = zoomed.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        

        self.screen.blit(zoomed, zoomed_rect)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def intro_screen(self):
        pass
