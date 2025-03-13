import pygame

from configs.screen_config import *
from sprites.button import *


class FactionMenu:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.bg_image = pygame.image.load('img/ui_images/menu_bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))

        self.title = self.game.font_lg.render('Select your faction.', True, (200, 200, 200))
        self.title_rect = self.title.get_rect(centerx=SCREEN_WIDTH/2, centery=50)

        self.brit_flag = pygame.image.load('img/ui_images/british_flag.jpg').convert()
        self.brit_flag = pygame.transform.scale(self.brit_flag, (200, 100))
        self.brit_flag_rect = self.brit_flag.get_rect(x=100, y=100)
        self.britain_button = Button(self.game, 100, 200, 200, 40, BLACK, (180, 180, 180), 'Great Britain', 22)
        self.french_flag = pygame.image.load('img/ui_images/french_flag.jpg').convert()
        self.french_flag = pygame.transform.scale(self.french_flag, (200, 100))
        self.french_flag_rect = self.french_flag.get_rect(x=400, y=100)
        self.france_button = Button(self.game, 400, 200, 200, 40, BLACK, (180, 180, 180), 'France', 22)
        self.german_flag = pygame.image.load('img/ui_images/german_flag.jpg').convert()
        self.german_flag = pygame.transform.scale(self.german_flag, (200, 100))
        self.german_flag_rect = self.german_flag.get_rect(x=700, y=100)
        self.germany_button = Button(self.game, 700, 200, 200, 40, BLACK, (180, 180, 180), 'Germany', 22)
        self.aus_hung_flag = pygame.image.load('img/ui_images/austro_hungarian_flag.jpg').convert()
        self.aus_hung_flag = pygame.transform.scale(self.aus_hung_flag, (200, 100))
        self.aus_hung_flag_rect = self.aus_hung_flag.get_rect(x=1000, y=100)
        self.aus_hung_button = Button(self.game, 1000, 200, 200, 40, BLACK, (180, 180, 180), 'Austria-Hungary', 22)

        self.back_button = Button(self.game, 1050, 600, 200, 40, BLACK, (180, 180, 180), 'Back', 22)

        self.faction_menu = True
        
        self.button_timer = pygame.time.get_ticks()

        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.game.playing = False
                self.game.running = False
                self.faction_menu = False
                self.game.main_menu()

        

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()
        
        if now - self.button_timer >= 500:
            if self.back_button.is_pressed(mouse_pos, mouse_pressed):
                self.faction_menu = False
                self.game.main_menu()
            if self.britain_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.faction = 'Britain'
                self.faction_menu = False
                self.game.main_menu()
            if self.france_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.faction = 'France'
                self.faction_menu = False
                self.game.main_menu()
            if self.germany_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.faction = 'Germany'
                self.faction_menu = False
                self.game.main_menu()
            if self.aus_hung_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.faction = 'Aus-Hung'
                self.faction_menu = False
                self.game.main_menu()


    def update(self):

        pass

        

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.fill(BLACK)
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.brit_flag, self.brit_flag_rect)
        self.screen.blit(self.britain_button.image, self.britain_button.rect)
        self.screen.blit(self.french_flag, self.french_flag_rect)
        self.screen.blit(self.france_button.image, self.france_button.rect)
        self.screen.blit(self.german_flag, self.german_flag_rect)
        self.screen.blit(self.germany_button.image, self.germany_button.rect)
        self.screen.blit(self.aus_hung_flag, self.aus_hung_flag_rect)
        self.screen.blit(self.aus_hung_button.image, self.aus_hung_button.rect)
        self.screen.blit(self.back_button.image, self.back_button.rect)


        if self.britain_button.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, GREEN, (self.britain_button.x-3, self.britain_button.y-103, self.britain_button.width+6, self.britain_button.height+106), 3, border_radius=5)
        if self.france_button.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, GREEN, (self.france_button.x-3, self.france_button.y-103, self.france_button.width+6, self.france_button.height+106), 3, border_radius=5)
        if self.germany_button.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, GREEN, (self.germany_button.x-3, self.germany_button.y-103, self.germany_button.width+6, self.germany_button.height+106), 3, border_radius=5)
        if self.aus_hung_button.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, GREEN, (self.aus_hung_button.x-3, self.aus_hung_button.y-103, self.aus_hung_button.width+6, self.aus_hung_button.height+106), 3, border_radius=5)
        if self.back_button.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, GREEN, (self.back_button.x-3, self.back_button.y-3, self.back_button.width+6, self.back_button.height+6), 3, border_radius=5)



        self.screen.blit(self.game.mouse, mouse_pos)

        self.game.clock.tick(FPS)
        pygame.display.update()

    def loop(self):
        while self.faction_menu:
            self.events()
            self.update()
            self.draw()