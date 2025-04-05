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
        self.width = 160
        self.height = 40

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(BLACK)
        
        self.image = pygame.transform.scale_by(self.game.minimap_buffer, 0.09)
        self.surf.blit(self.image, (0, 0))
        
        self.rect = self.surf.get_rect(x=self.x, y=self.y)
        

        for sprite in sorted(self.game.bottom_sprites, key= lambda sprite: sprite.rect.centery):
            if sprite.rect.collidepoint((0, 0)):
                self.ref_rect = sprite

        self.small_rect_x = (((self.ref_rect.init_x/4160)*self.width)+20)*1.2
        self.small_rect_y = (((self.ref_rect.init_y/1920)*self.height)+10)*1.6

        self.small_rect = pygame.Surface((TILESIZE/self.game.zoom_level, (TILESIZE/2)/self.game.zoom_level))
        self.small_rect.fill(WHITE)
        self.small_rect.set_alpha(128)


    def update(self):
        
        self.image = pygame.transform.scale_by(self.game.minimap_buffer, 0.09)

        for sprite in sorted(self.game.bottom_sprites, key= lambda sprite: sprite.rect.centery):
            if sprite.rect.collidepoint((0, 0)):
                self.small_rect_x = (((sprite.init_x/4160)*self.width)+20)*1.2
                self.small_rect_y = (((sprite.init_y/1920)*self.height)+10)*1.6

        self.small_rect = pygame.Surface((TILESIZE/self.game.zoom_level, (TILESIZE/2)/self.game.zoom_level))
        self.small_rect.fill(WHITE)
        self.small_rect.set_alpha(128)

    def draw(self):
        self.surf.fill(BLACK)
        self.surf.blit(self.image, (0, 0))
        #   self.surf.blit(self.small_rect, (self.small_rect_x, self.small_rect_y))
        self.screen.blit(self.surf, (self.x, self.y))

    