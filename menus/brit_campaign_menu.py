import pygame

from configs.screen_config import *
from sprites.button import *
from menus.faction_text import *


class BritCampaignMenu:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.bg_image = pygame.image.load('img/ui_images/brit_campaign_bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.green_rect = pygame.image.load('img/ui_images/main_menu_rect.png').convert_alpha()
        self.green_rect_rect = self.green_rect.get_rect(x=SCREEN_WIDTH-350, y=280)

        self.title = self.game.font_lg.render('Campaign - Great Britain', True, GREEN)
        self.title_rect = self.title.get_rect(centerx=SCREEN_WIDTH/2, centery=50)

        
        self.brit_flag = pygame.image.load('img/ui_images/british_flag.jpg').convert()
        self.brit_flag = pygame.transform.scale(self.brit_flag, (200, 100))
        self.brit_flag_rect = self.brit_flag.get_rect(centerx=SCREEN_WIDTH/2, centery=120)
        
        self.back_button = Button(self.game, 1080, 600, 200, 40, BLACK, (180, 180, 180), 'Back', 22)

        self.brit_campaign_menu = True
        
        self.button_timer = pygame.time.get_ticks()
        self.faction_description = ''

        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.game.playing = False
                self.game.running = False
                self.brit_campaign_menu = False
                

        

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()
        
        if now - self.button_timer >= 500:
            if self.back_button.is_pressed(mouse_pos, mouse_pressed):
                self.brit_campaign_menu = False

    def update(self):
        pass

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.fill(BLACK)
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.brit_flag, self.brit_flag_rect)
        self.screen.blit(self.green_rect, self.green_rect_rect)
        
        self.screen.blit(self.back_button.image, self.back_button.rect)

        if self.back_button.rect.collidepoint(mouse_pos):
            self.back_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.back_button.x-3, self.back_button.y-3, self.back_button.width+6, self.back_button.height+6), 3, border_radius=5)
        


        self.screen.blit(self.game.mouse, mouse_pos)

        self.game.clock.tick(FPS)
        pygame.display.update()

    def loop(self):
        while self.brit_campaign_menu:
            self.events()
            self.update()
            self.draw()
