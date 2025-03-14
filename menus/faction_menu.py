import pygame

from configs.screen_config import *
from sprites.button import *
from menus.faction_text import *


class FactionMenu:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.bg_image = pygame.image.load('img/ui_images/menu_bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))

        self.title = self.game.font_lg.render('Select your faction.', True, GREEN)
        self.title_rect = self.title.get_rect(centerx=SCREEN_WIDTH/2, centery=50)

        self.faction_description = ''

        self.description_text = self.game.font.render(f'{self.faction_description}', True, (200, 200, 200))
        self.description_text_rect = self.description_text.get_rect(x=100, y=300)

        self.unit_list_text = ''

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
        
        self.back_button = Button(self.game, 1050, 600, 200, 40, BLACK, (180, 180, 180), 'Back', 22)

        self.faction_menu = True
        
        self.button_timer = pygame.time.get_ticks()
        self.faction_description = ''

        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.game.playing = False
                self.game.running = False
                self.faction_menu = False
                

        

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()
        
        if now - self.button_timer >= 500:
            if self.back_button.is_pressed(mouse_pos, mouse_pressed):
                self.faction_menu = False
                
            if self.britain_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.faction = 'Britain'
                
                
            if self.france_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.faction = 'France'
                
                
            if self.germany_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.faction = 'Germany'
                
                
            
                
                


    def update(self):
        if self.game.faction == 'Britain':
            self.faction_description = GREAT_BRITAIN_DESCRIPTION
            self.unit_list_text = GREAT_BRITAIN_UNIT_LIST
        if self.game.faction == 'France':
            self.faction_description = FRANCE_DESCRIPTION
            self.unit_list_text = FRANCE_UNIT_LIST
        if self.game.faction == 'Germany':
            self.faction_description = GERMANY_DESCRIPTION
            self.unit_list_text = GERMANY_UNIT_LIST

        try:
            self.description_text = self.game.font_lg.render(f'{self.faction_description[0]}', True, GREEN)
            self.description_text_rect = self.description_text.get_rect(x=100, y=280)
            self.description_text2 = self.game.font.render(f'{self.faction_description[1]}', True, GREEN)
            self.description_text_rect2 = self.description_text2.get_rect(x=100, y=320)
            self.description_text3 = self.game.font.render(f'{self.faction_description[2]}', True, GREEN)
            self.description_text_rect3 = self.description_text3.get_rect(x=100, y=340)
            self.description_text4 = self.game.font.render(f'{self.faction_description[3]}', True, GREEN)
            self.description_text_rect4 = self.description_text4.get_rect(x=100, y=360)
            self.description_text5 = self.game.font.render(f'{self.faction_description[4]}', True, GREEN)
            self.description_text_rect5 = self.description_text5.get_rect(x=100, y=380)
            self.description_text6 = self.game.font.render(f'{self.faction_description[5]}', True, GREEN)
            self.description_text_rect6 = self.description_text6.get_rect(x=100, y=400)
            self.description_text7 = self.game.font.render(f'{self.faction_description[6]}', True, GREEN)
            self.description_text_rect7 = self.description_text7.get_rect(x=100, y=420)
            self.description_text8 = self.game.font.render(f'{self.faction_description[7]}', True, GREEN)
            self.description_text_rect8 = self.description_text8.get_rect(x=100, y=440)
            self.description_text9 = self.game.font.render(f'{self.faction_description[8]}', True, GREEN)
            self.description_text_rect9 = self.description_text9.get_rect(x=100, y=460)

        except IndexError:
            pass

        try:
            self.unit_list_label = self.game.font_lg.render('Unit List:', True, GREEN)
            self.unit_list_label_rect = self.unit_list_label.get_rect(x=1060, y=310)
            self.unit_list = self.game.font.render(f'{self.unit_list_text[0]}', True, GREEN)
            self.unit_list_rect = self.unit_list.get_rect(x=1060, y=350)
            self.unit_list2 = self.game.font.render(f'{self.unit_list_text[1]}', True, GREEN)
            self.unit_list_rect2 = self.unit_list2.get_rect(x=1060, y=370)
            self.unit_list3 = self.game.font.render(f'{self.unit_list_text[2]}', True, GREEN)
            self.unit_list_rect3 = self.unit_list3.get_rect(x=1060, y=390)
            self.unit_list4 = self.game.font.render(f'{self.unit_list_text[3]}', True, GREEN)
            self.unit_list_rect4 = self.unit_list4.get_rect(x=1060, y=410)
            self.unit_list5 = self.game.font.render(f'{self.unit_list_text[4]}', True, GREEN)
            self.unit_list_rect5 = self.unit_list5.get_rect(x=1060, y=430)
            self.unit_list6 = self.game.font.render(f'{self.unit_list_text[5]}', True, GREEN)
            self.unit_list_rect6 = self.unit_list6.get_rect(x=1060, y=450)
            self.unit_list7 = self.game.font.render(f'{self.unit_list_text[6]}', True, GREEN)
            self.unit_list_rect7 = self.unit_list7.get_rect(x=1060, y=470)
        except:
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
        
        self.screen.blit(self.back_button.image, self.back_button.rect)

        try:
            self.screen.blit(self.description_text, self.description_text_rect)
            self.screen.blit(self.description_text2, self.description_text_rect2)
            self.screen.blit(self.description_text3, self.description_text_rect3)
            self.screen.blit(self.description_text4, self.description_text_rect4)
            self.screen.blit(self.description_text5, self.description_text_rect5)
            self.screen.blit(self.description_text6, self.description_text_rect6)
            self.screen.blit(self.description_text7, self.description_text_rect7)
            self.screen.blit(self.description_text8, self.description_text_rect8)
            self.screen.blit(self.description_text9, self.description_text_rect9)

            self.screen.blit(self.unit_list_label, self.unit_list_label_rect)
            self.screen.blit(self.unit_list, self.unit_list_rect)
            self.screen.blit(self.unit_list2, self.unit_list_rect2)
            self.screen.blit(self.unit_list3, self.unit_list_rect3)
            self.screen.blit(self.unit_list4, self.unit_list_rect4)
            self.screen.blit(self.unit_list5, self.unit_list_rect5)
            self.screen.blit(self.unit_list6, self.unit_list_rect6)
            self.screen.blit(self.unit_list7, self.unit_list_rect7)
        except:
            pass


        if self.britain_button.rect.collidepoint(mouse_pos):
            self.britain_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.britain_button.x-3, self.britain_button.y-103, self.britain_button.width+6, self.britain_button.height+106), 3, border_radius=5)
        if self.france_button.rect.collidepoint(mouse_pos):
            self.france_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.france_button.x-3, self.france_button.y-103, self.france_button.width+6, self.france_button.height+106), 3, border_radius=5)
        if self.germany_button.rect.collidepoint(mouse_pos):
            self.germany_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.germany_button.x-3, self.germany_button.y-103, self.germany_button.width+6, self.germany_button.height+106), 3, border_radius=5)
        if self.back_button.rect.collidepoint(mouse_pos):
            self.back_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.back_button.x-3, self.back_button.y-3, self.back_button.width+6, self.back_button.height+6), 3, border_radius=5)
        try:
            if self.game.faction == 'Britain':
                pygame.draw.rect(self.screen, GREEN, (self.description_text_rect.x-10, self.description_text_rect2.y-10, 810, (self.description_text_rect.height*11)+10), 3, border_radius=5)
                pygame.draw.rect(self.screen, GREEN, (self.britain_button.x-3, self.britain_button.y-103, self.britain_button.width+6, self.britain_button.height+106), 3, border_radius=5)
                pygame.draw.rect(self.screen, GREEN, (self.unit_list_rect.x-10, self.unit_list_rect.y-10, 200, (self.unit_list_rect.height*8)+10), 3, border_radius=5)

            if self.game.faction == 'France':
                pygame.draw.rect(self.screen, GREEN, (self.description_text_rect.x-10, self.description_text_rect2.y-10, 810, (self.description_text_rect.height*11)+10), 3, border_radius=5)
                pygame.draw.rect(self.screen, GREEN, (self.france_button.x-3, self.france_button.y-103, self.france_button.width+6, self.france_button.height+106), 3, border_radius=5)
                pygame.draw.rect(self.screen, GREEN, (self.unit_list_rect.x-10, self.unit_list_rect.y-10, 200, (self.unit_list_rect.height*8)+10), 3, border_radius=5)

            if self.game.faction == 'Germany':
                pygame.draw.rect(self.screen, GREEN, (self.description_text_rect.x-10, self.description_text_rect2.y-10, 810, (self.description_text_rect.height*11)+10), 3, border_radius=5)
                pygame.draw.rect(self.screen, GREEN, (self.germany_button.x-3, self.germany_button.y-103, self.germany_button.width+6, self.germany_button.height+106), 3, border_radius=5)
                pygame.draw.rect(self.screen, GREEN, (self.unit_list_rect.x-10, self.unit_list_rect.y-10, 200, (self.unit_list_rect.height*8)+10), 3, border_radius=5)

        except:
            pass


        self.screen.blit(self.game.mouse, mouse_pos)

        self.game.clock.tick(FPS)
        pygame.display.update()

    def loop(self):
        while self.faction_menu:
            self.events()
            self.update()
            self.draw()
