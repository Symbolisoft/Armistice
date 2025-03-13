import pygame

from configs.screen_config import *

class Button:
    def __init__(self, game, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('jennifer.ttf', fontsize)
        self.content = content
        
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill(self.bg)

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center= (self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.highlight = 0

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

    
        