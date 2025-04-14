import pygame

from configs.screen_config import *
from configs.sprites_config import *


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
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

        self.images = [
            self.game.water_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE, 128),
            self.game.water_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE, 128),
            self.game.water_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE, 114),
            self.game.water_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE, 114),
            self.game.water_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE, 100),
            self.game.water_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE, 100)
        ]

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.animation_loop = 0
        self.animation_timer = pygame.time.get_ticks()

    def update(self):
        self.animate()
        self.x_dif = self.x - self.init_x
        self.y_dif = self.y - self.init_y
        
    def animate(self):
        self.image = self.images[math.floor(self.animation_loop)]
        self.animation_loop += 0.1
        if self.animation_loop >= 6:
            self.animation_loop = 0
