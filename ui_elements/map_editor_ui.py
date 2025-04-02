import pygame

from configs.screen_config import *
from sprites.button import *
from ui_elements.minimap import *


class MapUI:
    def __init__(self, game):
        
        self.game = game
        self.screen = self.game.screen

        self.bg_image = pygame.image.load('img/ui_images/map_ui.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.minimap = MiniMap(self.game, SCREEN_WIDTH-270, 520)

    def events(self):
        pass

    def update(self):
        self.minimap.update()

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.minimap.draw()