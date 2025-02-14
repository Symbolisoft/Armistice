import pygame
from configs.sprites_config import *

class ActiveTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = UI_LAYER
        self.groups = self.game.all_sprites, self.game.active_tile_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = 32
        self.height = 16

        self.image = self.game.active_tile_spritesheet.get_sprite(0, 0, 32, 16)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.timer = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.timer >= 200:
            self.kill()