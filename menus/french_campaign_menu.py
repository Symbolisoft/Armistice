import pygame

from configs.screen_config import *
from sprites.button import *
from menus.faction_text import *
from campaigns.campaigns import *


class FrenchCampaignMenu:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.bg_image = pygame.image.load('img/ui_images/french_campaign_bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.green_rect = pygame.image.load('img/ui_images/main_menu_rect.png').convert_alpha()
        self.green_rect = pygame.transform.scale(self.green_rect, (350, 600))
        self.green_rect_rect = self.green_rect.get_rect(centerx=SCREEN_WIDTH/2, y=150)

        self.title = self.game.font_lg.render('Campaign - France', True, GREEN)
        self.title_rect = self.title.get_rect(centerx=SCREEN_WIDTH/2, centery=50)

        self.line1 = self.game.font_lg.render(f'Mission {self.game.camp_level}:', True, GREEN)
        self.line1_rect = self.line1.get_rect(x=850, y=150)
        self.line2 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][0]}', True, GREEN)
        self.line2_rect = self.line2.get_rect(x=850, y=190)
        self.line3 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][1]}', True, GREEN)
        self.line3_rect = self.line3.get_rect(x=850, y=220)
        self.line4 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][2]}', True, GREEN)
        self.line4_rect = self.line4.get_rect(x=850, y=240)
        self.line5 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][3]}', True, GREEN)
        self.line5_rect = self.line5.get_rect(x=850, y=260)
        self.line6 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][4]}', True, GREEN)
        self.line6_rect = self.line6.get_rect(x=850, y=280)
        self.line7 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][5]}', True, GREEN)
        self.line7_rect = self.line7.get_rect(x=850, y=300)
        self.line8 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][6]}', True, GREEN)
        self.line8_rect = self.line8.get_rect(x=850, y=320)
        self.line9 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][7]}', True, GREEN)
        self.line9_rect = self.line9.get_rect(x=850, y=340)
        self.line10 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][8]}', True, GREEN)
        self.line10_rect = self.line10.get_rect(x=850, y=360)
        self.line11 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][9]}', True, GREEN)
        self.line11_rect = self.line11.get_rect(x=850, y=380)
        self.line12 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][10]}', True, GREEN)
        self.line12_rect = self.line12.get_rect(x=850, y=400)
        self.line13 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][11]}', True, GREEN)
        self.line13_rect = self.line13.get_rect(x=850, y=420)
        self.line14 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][12]}', True, GREEN)
        self.line14_rect = self.line14.get_rect(x=850, y=440)
        self.line15 = self.game.font.render(f'{FRENCH_CAMPAIGN[self.game.camp_level-1][13]}', True, GREEN)
        self.line15_rect = self.line15.get_rect(x=850, y=460)
        
        self.french_flag = pygame.image.load('img/ui_images/french_flag.jpg').convert()
        self.french_flag = pygame.transform.scale(self.french_flag, (200, 100))
        self.french_flag_rect = self.french_flag.get_rect(centerx=SCREEN_WIDTH/2, centery=120)
        
        self.new_button = Button(self.game, 580, 250, 200, 40, BLACK, (180, 180, 180), 'New Campaign', 22)
        self.continue_button = Button(self.game, 580, 300, 200, 40, BLACK, (180, 180, 180), 'Continue', 22)
        self.save_button = Button(self.game, 580, 350, 200, 40, BLACK, (180, 180, 180), 'Save Campaign', 22)
        self.load_button = Button(self.game, 580, 400, 200, 40, BLACK, (180, 180, 180), 'Load Campaign', 22)
        self.back_button = Button(self.game, 580, 600, 200, 40, BLACK, (180, 180, 180), 'Back', 22)

        self.french_campaign_menu = True
        
        self.button_timer = pygame.time.get_ticks()
        self.faction_description = ''

        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.game.playing = False
                self.game.running = False
                self.french_campaign_menu = False
                

        

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()
        
        if now - self.button_timer >= 500:
            if self.back_button.is_pressed(mouse_pos, mouse_pressed):
                self.french_campaign_menu = False

    def update(self):
        pass

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.fill(BLACK)
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.french_flag, self.french_flag_rect)
        self.screen.blit(self.green_rect, self.green_rect_rect)

        self.screen.blit(self.line1, self.line1_rect)
        self.screen.blit(self.line2, self.line2_rect)
        self.screen.blit(self.line3, self.line3_rect)
        self.screen.blit(self.line4, self.line4_rect)
        self.screen.blit(self.line5, self.line5_rect)
        self.screen.blit(self.line6, self.line6_rect)
        self.screen.blit(self.line7, self.line7_rect)
        self.screen.blit(self.line8, self.line8_rect)
        self.screen.blit(self.line9, self.line9_rect)
        self.screen.blit(self.line10, self.line10_rect)
        self.screen.blit(self.line11, self.line11_rect)
        self.screen.blit(self.line12, self.line12_rect)
        self.screen.blit(self.line13, self.line13_rect)
        self.screen.blit(self.line14, self.line14_rect)
        self.screen.blit(self.line15, self.line15_rect)
        
        self.screen.blit(self.continue_button.image, self.continue_button.rect)
        self.screen.blit(self.new_button.image, self.new_button.rect)
        self.screen.blit(self.save_button.image, self.save_button.rect)
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
        if self.continue_button.rect.collidepoint(mouse_pos):
            self.continue_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.continue_button.x-3, self.continue_button.y-3, self.continue_button.width+6, self.continue_button.height+6), 3, border_radius=5)
        if self.game.camp_level > 1:
            if self.save_button.rect.collidepoint(mouse_pos):
                self.save_button.fg = GREEN
                pygame.draw.rect(self.screen, GREEN, (self.save_button.x-3, self.save_button.y-3, self.save_button.width+6, self.save_button.height+6), 3, border_radius=5)
        

        self.screen.blit(self.game.mouse, mouse_pos)

        self.game.clock.tick(FPS)
        pygame.display.update()

    def loop(self):
        while self.french_campaign_menu:
            self.events()
            self.update()
            self.draw()
