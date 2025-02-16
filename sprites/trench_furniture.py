import pygame
import random
from sprites.spritesheet import *
from configs.sprites_config import *
from configs.screen_config import TILESIZE


class BunkRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.bunks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class BunkLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.bunks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class SandBagsRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.sandbags
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.trench_furnishings_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE),
            self.game.trench_furnishings_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE)
        ]

        self.image =  self.images[random.randint(0,1)]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class SandBagsLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.sandbags
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.trench_furnishings_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE),
            self.game.trench_furnishings_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE)
        ]

        self.image =  self.images[random.randint(0,1)]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class CabinetRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class CabinetLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class GunRackRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class GunRackLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(128, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class GreenCratesRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class GreenCratesLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(160, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class ArtyShellsRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class ArtyShellsLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class FiringStepRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.firing_steps
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class FiringStepLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.firing_steps
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class LadderRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(288, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class LadderLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.ladders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class BarbedWireRight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.barbed_wire
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class BarbedWireLeft(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FURNITURE_LAYER_2
        self.groups = self.game.all_sprites, self.game.barbed_wire
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  self.game.trench_furnishings_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


