import pygame

from sprites.button import *
from configs.screen_config import *
from menus.faction_menu import *
from menus.brit_campaign_menu import *



class MainMenu:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.bg_image = pygame.image.load('img/ui_images/cover-art-poppy.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.game.last_post.play(-1)

        self.faction_label = self.game.font.render(f'Selected Faction:  {self.game.faction}', True, (200, 200, 200))
        self.faction_label_rect = self.faction_label.get_rect(x=SCREEN_WIDTH-280, y=310)

        self.brit_flag = pygame.image.load('img/ui_images/british_flag.jpg').convert()
        self.brit_flag = pygame.transform.scale(self.brit_flag, (150, 75))
        self.french_flag = pygame.image.load('img/ui_images/french_flag.jpg').convert()
        self.french_flag = pygame.transform.scale(self.french_flag, (150, 75))
        self.german_flag = pygame.image.load('img/ui_images/german_flag.jpg').convert()
        self.german_flag = pygame.transform.scale(self.german_flag, (150, 75))
        self.aus_hung_flag = pygame.image.load('img/ui_images/austro_hungarian_flag.jpg').convert()
        self.aus_hung_flag = pygame.transform.scale(self.aus_hung_flag, (150, 75))

        self.flag = pygame.image.load('img/ui_images/empty.png')
        self.flag = pygame.transform.scale(self.flag, (150, 75))

        

        self.factions_button = Button(self.game, SCREEN_WIDTH-270, 430, 200, 40, BLACK, (180, 180, 180), 'Choose Faction', 22)
        self.campaign_button = Button(self.game, SCREEN_WIDTH-270, 475, 200, 40, BLACK, (180, 180, 180), 'Campaign', 22)
        self.skirmish_button = Button(self.game, SCREEN_WIDTH-270, 530, 200, 40, BLACK, (180, 180, 180), 'Skirmish', 22)
        self.map_editor_button = Button(self.game, SCREEN_WIDTH-270, 575, 200, 40, BLACK, (180, 180, 180), 'Map Editor', 22)
        self.settings_button = Button(self.game, SCREEN_WIDTH-270, 630, 200, 40, BLACK, (180, 180, 180), 'Settings', 22)

        self.main_menu = True
        self.green_rect = pygame.image.load('img/ui_images/main_menu_rect.png').convert_alpha()
        self.green_rect_rect = self.green_rect.get_rect(x=SCREEN_WIDTH-320, y=280)
        self.button_timer = pygame.time.get_ticks()

        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.game.playing = False
                self.game.running = False
                self.main_menu = False

        

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()
        if now - self.button_timer >= 500:
            if self.factions_button.is_pressed(mouse_pos, mouse_pressed):
                faction_menu = FactionMenu(self.game)    
                faction_menu.loop()
                self.button_timer = now
            if self.campaign_button.is_pressed(mouse_pos, mouse_pressed):
                if self.game.faction == 'Britain':
                    brit_campaign_menu = BritCampaignMenu(self.game)
                    brit_campaign_menu.loop()
                    self.button_timer = now
                if self.game.faction == 'France':
                    pass
                if self.game.faction == 'Germany':
                    pass
            if self.skirmish_button.is_pressed(mouse_pos, mouse_pressed):
                print('skirmish')
                self.button_timer = now
            if self.map_editor_button.is_pressed(mouse_pos, mouse_pressed):
                print('map editor')
                self.button_timer = now
            if self.settings_button.is_pressed(mouse_pos, mouse_pressed):
                print('settings')
                self.button_timer = now


    def update(self):

        self.faction_label = self.game.font.render(f'Selected Faction:  {self.game.faction}', True, (200, 200, 200))
        
        if self.game.faction == 'Britain':
            self.flag = self.brit_flag
        elif self.game.faction == 'France':
            self.flag = self.french_flag
        elif self.game.faction == 'Germany':
            self.flag = self.german_flag
        elif self.game.faction == 'Aus-Hung':
            self.flag = self.aus_hung_flag

        

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.fill(BLACK)
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.green_rect, self.green_rect_rect)
        pygame.draw.rect(self.screen, (140, 140, 140, 100), (SCREEN_WIDTH-245, 340, 150, 75), border_radius=3)
        self.screen.blit(self.faction_label, self.faction_label_rect)
        
        self.screen.blit(self.flag, (SCREEN_WIDTH-245, 340))
        self.screen.blit(self.factions_button.image, self.factions_button.rect)
        self.screen.blit(self.campaign_button.image, self.campaign_button.rect)
        self.screen.blit(self.skirmish_button.image, self.skirmish_button.rect)
        self.screen.blit(self.map_editor_button.image, self.map_editor_button.rect)
        self.screen.blit(self.settings_button.image, self.settings_button.rect)

            
        


        if self.factions_button.rect.collidepoint(mouse_pos):
            self.factions_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.factions_button.x-3, self.factions_button.y-3, self.factions_button.width+6, self.factions_button.height+6), 3, border_radius=5)
        if self.campaign_button.rect.collidepoint(mouse_pos):
            self.campaign_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.campaign_button.x-3, self.campaign_button.y-3, self.campaign_button.width+6, self.campaign_button.height+6), 3, border_radius=5)
        if self.skirmish_button.rect.collidepoint(mouse_pos):
            self.skirmish_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.skirmish_button.x-3, self.skirmish_button.y-3, self.skirmish_button.width+6, self.skirmish_button.height+6), 3, border_radius=5)
        if self.map_editor_button.rect.collidepoint(mouse_pos):
            self.map_editor_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.map_editor_button.x-3, self.map_editor_button.y-3, self.map_editor_button.width+6, self.map_editor_button.height+6), 3, border_radius=5)
        if self.settings_button.rect.collidepoint(mouse_pos):
            self.settings_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.settings_button.x-3, self.settings_button.y-3, self.settings_button.width+6, self.settings_button.height+6), 3, border_radius=5)

        
        
        self.screen.blit(self.game.mouse, mouse_pos)

        self.game.clock.tick(FPS)
        pygame.display.update()

    def loop(self):
        while self.main_menu:
            self.events()
            self.update()
            self.draw()