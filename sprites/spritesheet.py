import pygame
from configs.screen_config import *


class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()
        

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey(WHITE)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite


class AlphaSpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()
        

    def get_sprite(self, x, y, width, height, alpha_val):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey(WHITE)
        sprite.set_alpha(alpha_val)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite
