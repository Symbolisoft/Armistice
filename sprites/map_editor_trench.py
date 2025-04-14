import pygame

from configs.screen_config import *
from configs.sprites_config import *


class MapEdTrench1(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench2(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench3(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench4(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench5(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench6(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench7(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench8(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench9(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench10(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(288, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench11(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(320, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench12(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(352, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench13(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(384, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench14(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(416, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench15(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(448, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench16(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(480, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench17(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(512, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench18(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(544, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench19(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(576, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench20(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(608, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench25(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench26(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench27(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench28(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench29(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(128, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench30(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(160, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench31(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench32(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench33(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench34(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench35(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(320, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench36(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(352, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench37(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(384, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench38(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(416, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench39(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(448, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench40(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(480, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench41(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(512, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench42(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(544, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench43(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(576, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

class MapEdTrench44(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet.get_sprite(608, 32, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        

