import pygame

from configs.screen_config import *
from sprites.button import *


class MapUI:
    def __init__(self, game):
        
        self.game = game
        self.screen = self.game.screen

        self.bg_image = pygame.image.load('img/ui_images/map_ui.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))

    def events(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))