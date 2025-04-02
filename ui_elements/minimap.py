import pygame
import math

from configs.screen_config import *
from configs.sprites_config import *


class MiniMap:
    def __init__(self, game, x, y):
        self.game = game
        self.screen = self.game.screen

        self.x = x
        self.y = y
        self.width = 200
        self.height = 60

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(BLACK)
        self.rect = self.surf.get_rect(x=self.x, y=self.y)
        

        for sprite in sorted(self.game.bottom_sprites, key= lambda sprite: sprite.rect.centery):
            if sprite.rect.collidepoint((0, 0)):
                self.small_rect_x = ((sprite.init_x/4160)*self.width)+30
                self.small_rect_y = ((sprite.init_y/1920)*self.height)+30

        self.small_rect = pygame.Surface((40, 20))
        self.small_rect.fill(WHITE)


    def update(self):
        for sprite in sorted(self.game.bottom_sprites, key= lambda sprite: sprite.rect.centery):
            if sprite.rect.collidepoint((0, 0)):
                self.small_rect_x = ((sprite.init_x/4160)*self.width)+30
                self.small_rect_y = ((sprite.init_y/1920)*self.height)+20

    def draw(self):
        self.surf.fill(BLACK)
        self.surf.blit(self.small_rect, (self.small_rect_x, self.small_rect_y))
        self.screen.blit(self.surf, (self.x, self.y))

    