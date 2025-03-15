import pygame

from configs.screen_config import *
from sprites.button import *
from menus.faction_text import *


class GermanCampaignMenu:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.bg_image = pygame.image.load('img/ui_images/german_campaign_bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.green_rect = pygame.image.load('img/ui_images/main_menu_rect.png').convert_alpha()
        self.green_rect = pygame.transform.scale(self.green_rect, (350, 600))
        self.green_rect_rect = self.green_rect.get_rect(centerx=SCREEN_WIDTH/2, y=150)
        
        self.title = self.game.font_lg.render('Campaign - Germany', True, GREEN)
        self.title_rect = self.title.get_rect(centerx=SCREEN_WIDTH/2, centery=50)

        
        self.german_flag = pygame.image.load('img/ui_images/german_flag.jpg').convert()
        self.german_flag = pygame.transform.scale(self.german_flag, (200, 100))
        self.german_flag_rect = self.german_flag.get_rect(centerx=SCREEN_WIDTH/2, centery=120)
        
        self.new_button = Button(self.game, 580, 350, 200, 40, BLACK, (180, 180, 180), 'New Campaign', 22)
        self.load_button = Button(self.game, 580, 400, 200, 40, BLACK, (180, 180, 180), 'Load Campaign', 22)
        self.back_button = Button(self.game, 580, 600, 200, 40, BLACK, (180, 180, 180), 'Back', 22)

        self.german_campaign_menu = True
        
        self.button_timer = pygame.time.get_ticks()
        self.faction_description = ''

        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.game.playing = False
                self.game.running = False
                self.german_campaign_menu = False
                

        

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()
        
        if now - self.button_timer >= 500:
            if self.back_button.is_pressed(mouse_pos, mouse_pressed):
                self.german_campaign_menu = False

    def update(self):
        pass

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.fill(BLACK)
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.german_flag, self.german_flag_rect)
        self.screen.blit(self.green_rect, self.green_rect_rect)
        
        self.screen.blit(self.new_button.image, self.new_button.rect)
        self.screen.blit(self.load_button.image, self.load_button.rect)
        self.screen.blit(self.back_button.image, self.back_button.rect)

        if self.back_button.rect.collidepoint(mouse_pos):
            self.back_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.back_button.x-3, self.back_button.y-3, self.back_button.width+6, self.back_button.height+6), 3, border_radius=5)
        if self.new_button.rect.collidepoint(mouse_pos):
            self.new_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.new_button.x-3, self.new_button.y-3, self.new_button.width+6, self.new_button.height+6), 3, border_radius=5)
        if self.load_button.rect.collidepoint(mouse_pos):
            self.load_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.load_button.x-3, self.load_button.y-3, self.load_button.width+6, self.load_button.height+6), 3, border_radius=5)
        


        self.screen.blit(self.game.mouse, mouse_pos)

        self.game.clock.tick(FPS)
        pygame.display.update()

    def loop(self):
        while self.german_campaign_menu:
            self.events()
            self.update()
            self.draw()
