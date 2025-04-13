import pygame
import random

from configs.screen_config import *
from configs.sprites_config import *


class MapEdBunkRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.bunks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdBunkLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.bunks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdSandBagsSmallRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.sandbags
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_furnishings_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE)
        

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdSandBagsLargeRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.sandbags
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_furnishings_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE)
        

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdSandBagsSmallLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.sandbags
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_furnishings_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdSandBagsLargeLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.sandbags
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.trench_furnishings_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdCabinetRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdCabinetLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdGunRackRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdGunRackLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(128, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdGreenCratesRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdGreenCratesLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(160, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdArtyShellsRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdArtyShellsLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdFiringStepRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.firing_steps
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdFiringStepLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.firing_steps
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdLadderRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(288, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdLadderLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdBarbedWireRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.barbed_wire
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdBarbedWireLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.top_sprites, self.game.barbed_wire
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdBarrelsRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(320, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdBarrelsLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(320, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdMediCratesRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(352, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdMediCratesLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(352, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdTableWHelmetRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(384, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdTableWHelmetLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(384, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdWoodenChairRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(416, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdWoodenChairLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(416, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdTableSquareRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(448, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdTableSquareLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(448, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdTableLongRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(480, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y


class MapEdTableLongLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.init_x = self.x
        self.x_dif = 0
        self.y = y
        self.init_y = self.y
        self.y_dif = 0

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(480, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y

