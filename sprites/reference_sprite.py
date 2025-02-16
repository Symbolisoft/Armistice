import pygame

from configs.screen_config import TILESIZE
from configs.sprites_config import UI_LAYER


class ReferenceSprite(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = UI_LAYER
        self.groups = self.game.all_sprites, self.game.reference_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = 0
        self.y = 0
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass
        