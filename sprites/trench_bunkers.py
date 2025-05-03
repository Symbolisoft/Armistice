import pygame

from configs.screen_config import *
from configs.sprites_config import *


class BunkerDoorLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_1
        self.groups = self.game.all_sprites, self.game.bunker_doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_bunker_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class BunkerDoorRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_1
        self.groups = self.game.all_sprites, self.game.bunker_doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_bunker_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class HQDoorLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_1
        self.groups = self.game.all_sprites, self.game.hq_doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_bunker_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class HQDoorRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_1
        self.groups = self.game.all_sprites, self.game.hq_doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_bunker_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class BunkerWindowLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_1
        self.groups = self.game.all_sprites, self.game.bunker_doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_bunker_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class BunkerWindowRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_1
        self.groups = self.game.all_sprites, self.game.bunker_doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_bunker_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class BunkerWall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_1
        self.groups = self.game.all_sprites, self.game.bunker_doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_bunker_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


