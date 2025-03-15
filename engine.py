import pygame
import sys
import pickle
import tkinter
from tkinter import filedialog

from sprites.spritesheet import *
from sprites.dirt import *
from configs.screen_config import *
from map_translator import *
from menus.main_menu import *
from map_editor import *

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
        self.icon = pygame.image.load('img/ui_images/pointer_default.png')
        pygame.display.set_icon(self.icon)
        self.screen_buffer = pygame.Surface((SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.screen_buffer_rect = self.screen_buffer.get_rect(x=0, y=0)
        pygame.display.set_caption('Armistice')

        self.camera = Camera(self)
        self.faction = 'None'
        self.font = pygame.font.Font('jennifer.ttf', 18)
        self.font_lg = pygame.font.Font('jennifer.ttf', 26)

        #   sounds

        self.last_post = pygame.mixer.Sound('snd/last-post.wav')


        #   SPRITESHEETS

        self.dirt_spritesheet = SpriteSheet('img/terrain_spritesheets/dirt_spritesheet.png')
        self.dirt_spritesheet_dark = SpriteSheet('img/terrain_spritesheets/dirt_spritesheet_dark.png')
        self.active_tile_spritesheet = SpriteSheet('img/ui_images/active_tile.png')
        self.trench_furnishings_spritesheet = SpriteSheet('img/object_spritesheets/trench_furnishings_spritesheet.png')
        self.attack_pointer_spritesheet = SpriteSheet('img/ui_images/attack_pointer_spritesheet.png')
        self.move_pointer_spritesheet = SpriteSheet('img/ui_images/move_pointer_spritesheet.png')


        self.default_mouse = pygame.image.load('img/ui_images/pointer_default.png')

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

        pygame.mouse.set_visible(False)

        self.mouse = self.default_mouse

        self.unit_attack = False
        self.unit_attack_loop = 0
        self.unit_attack_cursor_animations = [
            self.attack_pointer_spritesheet.get_sprite(0, 0, 32, 32),
            self.attack_pointer_spritesheet.get_sprite(32, 0, 32, 32),
            self.attack_pointer_spritesheet.get_sprite(64, 0, 32, 32)
        ]


        self.unit_move = False
        self.unit_move_loop = 0
        self.unit_move_cursor_animations = [
            self.move_pointer_spritesheet.get_sprite(0, 0, 32, 32),
            self.move_pointer_spritesheet.get_sprite(32, 0, 32, 32),
            self.move_pointer_spritesheet.get_sprite(64, 0, 32, 32)
        ]

        self.map_editor_open = False

        self.all_sprites = []
        self.reference_sprite = []
        self.dirt_group = []
        self.active_tile_group = []
        self.bunks = []
        self.sandbags = []
        self.firing_steps = []
        self.ladders = []
        self.barbed_wire = []
        self.bottom_sprites = []
        self.top_sprites = []

    def map_editor(self):
        
        self.map_editor_open = True

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

        self.map_editor_window = MapEditor(self)
        while self.map_editor_open:
            self.map_editor_window.loop()

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

        if keys[pygame.K_LSHIFT]:
            self.camera_speed = self.camera_speed * 2
        else:
            self.camera_speed = self.camera_speed

        if keys[pygame.K_LCTRL]:
            #   ADD CONDITION :- if unit selected (once units are implemented)
            self.unit_attack = True
        else:
            self.unit_attack = False

        if keys[pygame.K_m]:
            #   CHANGE CONDITION TO ONCE UNIT SELECTED
            self.unit_move = True
        else:
            self.unit_move = False

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

        if self.unit_attack:
            self.mouse = self.unit_attack_cursor_animations[math.floor(self.unit_attack_loop)]
            self.unit_attack_loop += 0.5
            if self.unit_attack_loop >= 3:
                self.unit_attack_loop = 0
        elif self.unit_move:
            self.mouse = self.unit_move_cursor_animations[math.floor(self.unit_move_loop)]
            self.unit_move_loop += 0.5
            if self.unit_move_loop >= 3:
                self.unit_move_loop = 0
        else:
            self.mouse = self.default_mouse

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

        if self.unit_attack:
            self.screen.blit(self.mouse, (mouse_pos[0]-16, mouse_pos[1]-16))
        elif self.unit_move:
            self.screen.blit(self.mouse, (mouse_pos[0]-16, mouse_pos[1]-16))
        else:
            self.screen.blit(self.mouse, mouse_pos)

        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def main_menu(self):
        m = MainMenu(self)
        m.loop()
