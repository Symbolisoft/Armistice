import pygame

from configs.screen_config import *
from sprites.button import *
from ui_elements.minimap import *
from map_editor_mode_switch import mode_switch


class MapUI:
    def __init__(self, game, map_editor):
        
        self.game = game
        self.screen = self.game.screen
        self.map_editor = map_editor

        self.bg_image = pygame.image.load('img/ui_images/map_ui.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH-50, SCREEN_HEIGHT-80))
        self.minimap = MiniMap(self.game, SCREEN_WIDTH-250, 520)

        self.dig_button = Button(self.game, 20, 520, 180, 30, BLACK, WHITE, 'Dig Trench', 26)
        self.trench_button = Button(self.game, 220, 520, 180, 30, BLACK, WHITE, 'Trench Walls', 26)
        self.furnishings_button = Button(self.game, 420, 520, 180, 30, BLACK, WHITE, 'Furnishings', 26)
        self.buildings_button = Button(self.game, 620, 520, 180, 30, BLACK, WHITE, 'Buildings', 26)
        self.surface_button = Button(self.game, 820, 520, 180, 30, BLACK, WHITE, 'Surface', 26)
        self.button_timer = pygame.time.get_ticks()
        self.digging = False

        self.blank_32 = pygame.image.load('img/ui_images/empty32.png')
        
        self.sp_button_1 = SpriteButton(self.game, 20, 560, self.blank_32)
        self.sp_button_2 = SpriteButton(self.game, 60, 560, self.blank_32)
        self.sp_button_3 = SpriteButton(self.game, 100, 560, self.blank_32)
        self.sp_button_4 = SpriteButton(self.game, 140, 560, self.blank_32)
        self.sp_button_5 = SpriteButton(self.game, 180, 560, self.blank_32)
        self.sp_button_6 = SpriteButton(self.game, 220, 560, self.blank_32)
        self.sp_button_7 = SpriteButton(self.game, 260, 560, self.blank_32)
        self.sp_button_8 = SpriteButton(self.game, 300, 560, self.blank_32)
        self.sp_button_9 = SpriteButton(self.game, 340, 560, self.blank_32)
        self.sp_button_10 = SpriteButton(self.game, 380, 560, self.blank_32)
        self.sp_button_11 = SpriteButton(self.game, 420, 560, self.blank_32)
        self.sp_button_12 = SpriteButton(self.game, 460, 560, self.blank_32)
        self.sp_button_13 = SpriteButton(self.game, 500, 560, self.blank_32)
        self.sp_button_14 = SpriteButton(self.game, 540, 560, self.blank_32)
        self.sp_button_15 = SpriteButton(self.game, 580, 560, self.blank_32)
        self.sp_button_16 = SpriteButton(self.game, 620, 560, self.blank_32)
        self.sp_button_17 = SpriteButton(self.game, 660, 560, self.blank_32)
        self.sp_button_18 = SpriteButton(self.game, 700, 560, self.blank_32)
        self.sp_button_19 = SpriteButton(self.game, 740, 560, self.blank_32)
        self.sp_button_20 = SpriteButton(self.game, 780, 560, self.blank_32)
        self.sp_button_21 = SpriteButton(self.game, 820, 560, self.blank_32)
        self.sp_button_22 = SpriteButton(self.game, 860, 560, self.blank_32)
        self.sp_button_23 = SpriteButton(self.game, 900, 560, self.blank_32)
        self.sp_button_24 = SpriteButton(self.game, 940, 560, self.blank_32)

        self.sp_button2_1 = SpriteButton(self.game, 20, 600, self.blank_32)
        self.sp_button2_2 = SpriteButton(self.game, 60, 600, self.blank_32)
        self.sp_button2_3 = SpriteButton(self.game, 100, 600, self.blank_32)
        self.sp_button2_4 = SpriteButton(self.game, 140, 600, self.blank_32)
        self.sp_button2_5 = SpriteButton(self.game, 180, 600, self.blank_32)
        self.sp_button2_6 = SpriteButton(self.game, 220, 600, self.blank_32)
        self.sp_button2_7 = SpriteButton(self.game, 260, 600, self.blank_32)
        self.sp_button2_8 = SpriteButton(self.game, 300, 600, self.blank_32)
        self.sp_button2_9 = SpriteButton(self.game, 340, 600, self.blank_32)
        self.sp_button2_10 = SpriteButton(self.game, 380, 600, self.blank_32)
        self.sp_button2_11 = SpriteButton(self.game, 420, 600, self.blank_32)
        self.sp_button2_12 = SpriteButton(self.game, 460, 600, self.blank_32)
        self.sp_button2_13 = SpriteButton(self.game, 500, 600, self.blank_32)
        self.sp_button2_14 = SpriteButton(self.game, 540, 600, self.blank_32)
        self.sp_button2_15 = SpriteButton(self.game, 580, 600, self.blank_32)
        self.sp_button2_16 = SpriteButton(self.game, 620, 600, self.blank_32)
        self.sp_button2_17 = SpriteButton(self.game, 660, 600, self.blank_32)
        self.sp_button2_18 = SpriteButton(self.game, 700, 600, self.blank_32)
        self.sp_button2_19 = SpriteButton(self.game, 740, 600, self.blank_32)
        self.sp_button2_20 = SpriteButton(self.game, 780, 600, self.blank_32)
        self.sp_button2_21 = SpriteButton(self.game, 820, 600, self.blank_32)
        self.sp_button2_22 = SpriteButton(self.game, 860, 600, self.blank_32)
        self.sp_button2_23 = SpriteButton(self.game, 900, 600, self.blank_32)
        self.sp_button2_24 = SpriteButton(self.game, 940, 600, self.blank_32)

    def events(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if self.dig_button.is_pressed(mouse_pos, mouse_pressed):
            mode_switch(self.map_editor, 1)
        elif self.trench_button.is_pressed(mouse_pos, mouse_pressed):
            mode_switch(self.map_editor, 2)
        elif self.furnishings_button.is_pressed(mouse_pos, mouse_pressed):
            mode_switch(self.map_editor, 3)
        elif self.buildings_button.is_pressed(mouse_pos, mouse_pressed):
            mode_switch(self.map_editor, 4)
        elif self.surface_button.is_pressed(mouse_pos, mouse_pressed):
            mode_switch(self.map_editor, 5)
        

    def update(self):
        self.minimap.update()

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.bg_image, (0, 0))
        self.minimap.draw()
        self.screen.blit(self.dig_button.image, self.dig_button.rect)
        self.screen.blit(self.trench_button.image, self.trench_button.rect)
        self.screen.blit(self.furnishings_button.image, self.furnishings_button.rect)
        self.screen.blit(self.buildings_button.image, self.buildings_button.rect)
        self.screen.blit(self.surface_button.image, self.surface_button.rect)

        try:
            self.screen.blit(self.sp_button_1.image, self.sp_button_1.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_2.image, self.sp_button_2.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_3.image, self.sp_button_3.rect)
            self.screen.blit(self.sp_button_4.image, self.sp_button_4.rect)
            self.screen.blit(self.sp_button_5.image, self.sp_button_5.rect)
            self.screen.blit(self.sp_button_6.image, self.sp_button_6.rect)
            self.screen.blit(self.sp_button_7.image, self.sp_button_7.rect)
            self.screen.blit(self.sp_button_8.image, self.sp_button_8.rect)
            self.screen.blit(self.sp_button_9.image, self.sp_button_9.rect)
            self.screen.blit(self.sp_button_10.image, self.sp_button_10.rect)
            self.screen.blit(self.sp_button_11.image, self.sp_button_11.rect)
            self.screen.blit(self.sp_button_12.image, self.sp_button_12.rect)
            self.screen.blit(self.sp_button_13.image, self.sp_button_13.rect)
            self.screen.blit(self.sp_button_14.image, self.sp_button_14.rect)
            self.screen.blit(self.sp_button_15.image, self.sp_button_15.rect)
            self.screen.blit(self.sp_button_16.image, self.sp_button_16.rect)
            self.screen.blit(self.sp_button_17.image, self.sp_button_17.rect)
            self.screen.blit(self.sp_button_18.image, self.sp_button_18.rect)
            self.screen.blit(self.sp_button_19.image, self.sp_button_19.rect)
            self.screen.blit(self.sp_button_20.image, self.sp_button_20.rect)
            self.screen.blit(self.sp_button_21.image, self.sp_button_21.rect)
            self.screen.blit(self.sp_button_22.image, self.sp_button_22.rect)
            self.screen.blit(self.sp_button_23.image, self.sp_button_23.rect)
            self.screen.blit(self.sp_button_24.image, self.sp_button_24.rect)

            self.screen.blit(self.sp_button2_1.image, self.sp_button2_1.rect)
            self.screen.blit(self.sp_button2_2.image, self.sp_button2_2.rect)
            self.screen.blit(self.sp_button2_3.image, self.sp_button2_3.rect)
            self.screen.blit(self.sp_button2_4.image, self.sp_button2_4.rect)
            self.screen.blit(self.sp_button2_5.image, self.sp_button2_5.rect)
            self.screen.blit(self.sp_button2_6.image, self.sp_button2_6.rect)
            self.screen.blit(self.sp_button2_7.image, self.sp_button2_7.rect)
            self.screen.blit(self.sp_button2_8.image, self.sp_button2_8.rect)
            self.screen.blit(self.sp_button2_9.image, self.sp_button2_9.rect)
            self.screen.blit(self.sp_button2_10.image, self.sp_button2_10.rect)
            self.screen.blit(self.sp_button2_11.image, self.sp_button2_11.rect)
            self.screen.blit(self.sp_button2_12.image, self.sp_button2_12.rect)
            self.screen.blit(self.sp_button2_13.image, self.sp_button2_13.rect)
            self.screen.blit(self.sp_button2_14.image, self.sp_button2_14.rect)
            self.screen.blit(self.sp_button2_15.image, self.sp_button2_15.rect)
            self.screen.blit(self.sp_button2_16.image, self.sp_button2_16.rect)
            self.screen.blit(self.sp_button2_17.image, self.sp_button2_17.rect)
            self.screen.blit(self.sp_button2_18.image, self.sp_button2_18.rect)
            self.screen.blit(self.sp_button2_19.image, self.sp_button2_19.rect)
            self.screen.blit(self.sp_button2_20.image, self.sp_button2_20.rect)
            self.screen.blit(self.sp_button2_21.image, self.sp_button2_21.rect)
            self.screen.blit(self.sp_button2_22.image, self.sp_button2_22.rect)
            self.screen.blit(self.sp_button2_23.image, self.sp_button2_23.rect)
            self.screen.blit(self.sp_button2_24.image, self.sp_button2_24.rect)
        except:
            pass

        if self.dig_button.rect.collidepoint(mouse_pos):
            self.dig_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.dig_button.x-3, self.dig_button.y-3, self.dig_button.width+6, self.dig_button.height+6), 3, border_radius=5)
        if self.trench_button.rect.collidepoint(mouse_pos):
            self.trench_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.trench_button.x-3, self.trench_button.y-3, self.trench_button.width+6, self.trench_button.height+6), 3, border_radius=5)
        if self.furnishings_button.rect.collidepoint(mouse_pos):
            self.furnishings_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.furnishings_button.x-3, self.furnishings_button.y-3, self.furnishings_button.width+6, self.furnishings_button.height+6), 3, border_radius=5)
        if self.buildings_button.rect.collidepoint(mouse_pos):
            self.buildings_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.buildings_button.x-3, self.buildings_button.y-3, self.buildings_button.width+6, self.buildings_button.height+6), 3, border_radius=5)
        if self.surface_button.rect.collidepoint(mouse_pos):
            self.surface_button.fg = GREEN
            pygame.draw.rect(self.screen, GREEN, (self.surface_button.x-3, self.surface_button.y-3, self.surface_button.width+6, self.surface_button.height+6), 3, border_radius=5)
