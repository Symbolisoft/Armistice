import pygame
import random

from configs.sprites_config import *
from configs.screen_config import TILESIZE
from sprites.active_tile import *


class Dirt1(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_1
        self.groups = self.game.bottom_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.init_x = self.x
        self.x_dif = 0
        self.y = (y-24)*(TILESIZE/2)
        self.init_y = self.y
        self.y_dif = 0
        self.width = TILESIZE/4
        self.height = TILESIZE/4

        self.images = [
            self.game.dirt_spritesheet_dark.get_sprite(0, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(32, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(64, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(96, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(128, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(160, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(192, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(224, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet_dark.get_sprite(256, 0, TILESIZE, TILESIZE)                            
                       ]
        
        self.image = self.images[random.randint(0, 8)]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y



class Dirt2(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.init_x = self.x
        self.x_dif = 0
        self.y = (y-24)*(TILESIZE/2)
        self.init_y = self.y
        self.y_dif = 0
        self.width = TILESIZE/4
        self.height = TILESIZE/4

        self.images = [
            self.game.dirt_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE)                            
                       ]
        
        self.image = self.images[random.randint(0, 8)]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.active_timer = pygame.time.get_ticks()

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y

        

    