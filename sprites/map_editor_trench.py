import pygame

from configs.screen_config import *
from configs.sprites_config import *


class MapEdDirt1(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = UI_LAYER
        self.groups = self.game.map_editor_build_sprite

        pygame.sprite.Sprite.__init__(self, self.groups)

        mouse_pos = pygame.mouse.get_pos()
        
        self.x = mouse_pos[0]
        self.y = mouse_pos[1]

        self.width = TILESIZE*self.game.zoom_level
        self.height = TILESIZE*self.game.zoom_level

        self.image = self.game.dirt_spritesheet_dark.get_sprite(0, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]
        self.rect.width = TILESIZE*self.game.zoom_level
        self.rect.height = TILESIZE*self.game.zoom_level
