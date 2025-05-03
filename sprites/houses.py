import pygame

from configs.screen_config import *
from configs.sprites_config import *


class House1(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.buildings
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = 64*self.game.zoom_level
        self.height = 64*self.game.zoom_level

        self.image = self.game.houses_spritesheet.get_sprite(0, 0, 64, 64)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class House2(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.buildings
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = 64*self.game.zoom_level
        self.height = 64*self.game.zoom_level

        self.image = self.game.houses_spritesheet.get_sprite(64, 0, 64, 64)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class House3(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.buildings
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = 64*self.game.zoom_level
        self.height = 64*self.game.zoom_level

        self.image = self.game.houses_spritesheet.get_sprite(128, 0, 64, 64)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

