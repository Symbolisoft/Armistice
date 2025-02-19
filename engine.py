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

        self.camera_speed = 16
        self.zoom_level = 1.3
        self.delta_time = 1

        self.drawing = False

        self.start_pos = 0
        self.end_pos = 0
        self.selection_rect = 0

    def new_game(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.reference_sprite = pygame.sprite.LayeredUpdates()
        self.dirt_group = pygame.sprite.LayeredUpdates()
        self.active_tile_group = pygame.sprite.LayeredUpdates()
        self.bunks = pygame.sprite.LayeredUpdates()
        self.sandbags = pygame.sprite.LayeredUpdates()
        self.firing_steps = pygame.sprite.LayeredUpdates()
        self.ladders = pygame.sprite.LayeredUpdates()
        self.barbed_wire = pygame.sprite.LayeredUpdates()
        self.bottom_sprites = pygame.sprite.LayeredUpdates()
        self.top_sprites = pygame.sprite.LayeredUpdates()

        

        
        self.ground_map_layer_2 = ground_map_translator(self, 'data/maps/ground_map.amf')
        self.funiture_map = furniture_map_translator(self, 'data/maps/furniture_map.amf')

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.playing = False
                self.running = False

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    if self.zoom_level < 1.8:
                        self.zoom_level += 0.05
                    else: 
                        self.zoom_level = 1.8
                if event.y < 0:
                    if self.zoom_level > 0.9:
                        self.zoom_level -= 0.05
                    else:
                        self.zoom_level = 0.9

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_pos = event.pos
                self.drawing = True
        
            if event.type == pygame.MOUSEMOTION and self.drawing:
                self.end_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                self.end_pos = 0
                self.start_pos = 0
                self.drawing = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            self.digging = True
        else:
            self.digging = False

        if keys[pygame.K_UP]:
            if self.zoom_level < 1.8:
                self.zoom_level += 0.05
            else: 
                self.zoom_level = 1.8
        if keys[pygame.K_DOWN]:
            if self.zoom_level > 0.9:
                self.zoom_level -= 0.05
            else:
                self.zoom_level = 0.9

    def update(self):
        
        self.bottom_sprites.update()
        self.all_sprites.update()
        self.top_sprites.update()
        self.camera.update()


        if self.zoom_level > 1.8:
            self.zoom_level = 1.8
        elif self.zoom_level < 0.9:
            self.zoom_level = 0.9

        self.camera_speed = self.camera_speed/(self.zoom_level)
        if self.camera_speed >= 8:
            self.camera_speed = 8
        if self.camera_speed <= 4:
            self.camera_speed = 4

    def draw(self):
        self.screen.fill(BLACK)
        self.screen_buffer.fill(BLACK)
        
        for sprite in self.bottom_sprites:
            if self.screen.get_rect().colliderect(sprite.rect):
                #   self.screen_buffer.blit(sprite.image, sprite.rect)
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

        for sprite in sorted(self.all_sprites, key= lambda sprite: sprite.rect.centery):
            if self.screen.get_rect().colliderect(sprite.rect):
                #   self.screen_buffer.blit(sprite.image, sprite.rect)
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

                if sprite == Dirt2 or TrenchLeftRecess or TrenchRightRecess or TrenchLeftTaperTop or TrenchRightTaperBottom or TrenchLeftTaperBottom or TrenchRightTaperTop or TrenchWalls1:
                    mouse_pos = pygame.mouse.get_pos()
                    hits = scaled_rect.collidepoint(mouse_pos)
                    if hits:
                        if self.digging:
                            ActiveTile(self, sprite.rect.x+sprite.x_dif, sprite.rect.y+sprite.y_dif)

        for sprite in sorted(self.top_sprites, key= lambda sprite: sprite.rect.centery):
            if self.screen.get_rect().colliderect(sprite.rect):
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

        if self.start_pos and self.end_pos:
            rect_width = self.end_pos[0] - self.start_pos[0]
            rect_height = self.end_pos[1] - self.start_pos[1]
            self.selection_rect = pygame.draw.rect(self.screen, GREEN, (self.start_pos[0], self.start_pos[1], rect_width, rect_height), 2)
        else:
            self.selection_rect = 0

        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def intro_screen(self):
        pass
