import pygame

from configs.screen_config import *
from sprites.button import *
from sprites.map_editor_trench import *
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

        self.build_sprite = 0
        

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
        
        if self.map_editor.mode == 'trench walls':
            if self.sp_button_1.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 1
            elif self.sp_button_2.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 2
            elif self.sp_button_3.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 3
            elif self.sp_button_4.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 4
            elif self.sp_button_5.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 5
            elif self.sp_button_6.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 6
            elif self.sp_button_7.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 7
            elif self.sp_button_8.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 8
            elif self.sp_button_9.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 9
            elif self.sp_button_10.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 10
            elif self.sp_button_11.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 11
            elif self.sp_button_12.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 12
            elif self.sp_button_13.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 13
            elif self.sp_button_14.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 14
            elif self.sp_button_15.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 15
            elif self.sp_button_16.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 16
            elif self.sp_button_17.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 17
            elif self.sp_button_18.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 18
            elif self.sp_button_19.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 19
            elif self.sp_button_21.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 21
            elif self.sp_button_20.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 20
            elif self.sp_button_22.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 22
            elif self.sp_button_23.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 23
            elif self.sp_button_24.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 24

            elif self.sp_button2_1.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 25
            elif self.sp_button2_2.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 26
            elif self.sp_button2_3.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 27
            elif self.sp_button2_4.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 28
            elif self.sp_button2_5.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 29
            elif self.sp_button2_6.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 30
            elif self.sp_button2_7.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 31
            elif self.sp_button2_8.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 32
            elif self.sp_button2_9.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 33
            elif self.sp_button2_10.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 34
            elif self.sp_button2_11.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 35
            elif self.sp_button2_12.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 36
            elif self.sp_button2_13.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 37
            elif self.sp_button2_14.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 38
            elif self.sp_button2_15.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 39
            elif self.sp_button2_16.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 40
            elif self.sp_button2_17.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 41
            elif self.sp_button2_18.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 42
            elif self.sp_button2_19.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 43
            elif self.sp_button2_20.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 44
            elif self.sp_button2_21.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 45
            elif self.sp_button2_22.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 46
            elif self.sp_button2_23.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 47
        elif self.map_editor.mode == 'furnishings':
            if self.sp_button_1.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 41
            elif self.sp_button_2.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 42
            elif self.sp_button_3.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 43
            elif self.sp_button_4.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 44
            elif self.sp_button_5.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 45
            elif self.sp_button_6.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 46
            elif self.sp_button_7.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 47
            elif self.sp_button_8.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 48
            elif self.sp_button_9.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 49
            elif self.sp_button_10.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 50
            elif self.sp_button_11.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 51
            elif self.sp_button_12.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 52
            elif self.sp_button_13.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 53
            elif self.sp_button_14.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 54
            elif self.sp_button_15.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 55
            elif self.sp_button_16.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 56
            elif self.sp_button_17.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 57
            elif self.sp_button_18.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 58
            elif self.sp_button_19.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 59
            elif self.sp_button_20.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 60
            elif self.sp_button_21.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 61
            elif self.sp_button_22.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 62
            elif self.sp_button_23.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 63
            elif self.sp_button_24.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 64

            elif self.sp_button2_1.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 65
            elif self.sp_button2_2.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 66
            elif self.sp_button2_3.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 67
            elif self.sp_button2_4.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 68
            elif self.sp_button2_5.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 69
            elif self.sp_button2_6.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 70
            elif self.sp_button2_7.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 71
            elif self.sp_button2_8.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 72
            elif self.sp_button2_9.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 73
            elif self.sp_button2_10.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 74
            elif self.sp_button2_11.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 75
            elif self.sp_button2_12.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 76
            elif self.sp_button2_13.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 77
            elif self.sp_button2_14.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 78
            elif self.sp_button2_15.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 79
            elif self.sp_button2_16.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 80
            elif self.sp_button2_17.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 81
            elif self.sp_button2_18.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 82
            elif self.sp_button2_19.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 83
            elif self.sp_button2_21.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 84
            elif self.sp_button2_22.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 85
            elif self.sp_button2_23.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 86
            elif self.sp_button2_24.is_pressed(mouse_pos, mouse_pressed):
                self.build_sprite = 87

        

    def update(self):
        self.minimap.update()

        if self.map_editor.mode == 'trench walls':
            self.sp_button_1 = SpriteButton(self.game, 20, 560, self.game.dirt_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE))
            self.sp_button_2 = SpriteButton(self.game, 60, 560, self.game.dirt_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE))
            self.sp_button_3 = SpriteButton(self.game, 100, 560, self.game.dirt_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE))
            self.sp_button_4 = SpriteButton(self.game, 140, 560, self.game.dirt_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE))
            self.sp_button_5 = SpriteButton(self.game, 180, 560, self.game.dirt_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE))
            self.sp_button_6 = SpriteButton(self.game, 220, 560, self.game.dirt_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE))
            self.sp_button_7 = SpriteButton(self.game, 260, 560, self.game.dirt_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE))
            self.sp_button_8 = SpriteButton(self.game, 300, 560, self.game.dirt_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE))
            self.sp_button_9 = SpriteButton(self.game, 340, 560, self.game.dirt_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE))
            self.sp_button_10 = SpriteButton(self.game, 380, 560, self.game.dirt_spritesheet.get_sprite(288, 0, TILESIZE, TILESIZE))
            self.sp_button_11 = SpriteButton(self.game, 420, 560, self.game.dirt_spritesheet.get_sprite(320, 0, TILESIZE, TILESIZE))
            self.sp_button_12 = SpriteButton(self.game, 460, 560, self.game.dirt_spritesheet.get_sprite(352, 0, TILESIZE, TILESIZE))
            self.sp_button_13 = SpriteButton(self.game, 500, 560, self.game.dirt_spritesheet.get_sprite(384, 0, TILESIZE, TILESIZE))
            self.sp_button_14 = SpriteButton(self.game, 540, 560, self.game.dirt_spritesheet.get_sprite(416, 0, TILESIZE, TILESIZE))
            self.sp_button_15 = SpriteButton(self.game, 580, 560, self.game.dirt_spritesheet.get_sprite(448, 0, TILESIZE, TILESIZE))
            self.sp_button_16 = SpriteButton(self.game, 620, 560, self.game.dirt_spritesheet.get_sprite(480, 0, TILESIZE, TILESIZE))
            self.sp_button_17 = SpriteButton(self.game, 660, 560, self.game.dirt_spritesheet.get_sprite(512, 0, TILESIZE, TILESIZE))
            self.sp_button_18 = SpriteButton(self.game, 700, 560, self.game.dirt_spritesheet.get_sprite(544, 0, TILESIZE, TILESIZE))
            self.sp_button_19 = SpriteButton(self.game, 740, 560, self.game.dirt_spritesheet.get_sprite(576, 0, TILESIZE, TILESIZE))
            self.sp_button_20 = SpriteButton(self.game, 780, 560, self.game.dirt_spritesheet.get_sprite(608, 0, TILESIZE, TILESIZE))
            self.sp_button_21 = SpriteButton(self.game, 820, 560, self.blank_32)
            self.sp_button_22 = SpriteButton(self.game, 860, 560, self.blank_32)
            self.sp_button_23 = SpriteButton(self.game, 900, 560, self.blank_32)
            self.sp_button_24 = SpriteButton(self.game, 940, 560, self.blank_32)

            self.sp_button2_1 = SpriteButton(self.game, 20, 600, self.game.dirt_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE))
            self.sp_button2_2 = SpriteButton(self.game, 60, 600, self.game.dirt_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE))
            self.sp_button2_3 = SpriteButton(self.game, 100, 600, self.game.dirt_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE))
            self.sp_button2_4 = SpriteButton(self.game, 140, 600, self.game.dirt_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE))
            self.sp_button2_5 = SpriteButton(self.game, 180, 600, self.game.dirt_spritesheet.get_sprite(128, 32, TILESIZE, TILESIZE))
            self.sp_button2_6 = SpriteButton(self.game, 220, 600, self.game.dirt_spritesheet.get_sprite(160, 32, TILESIZE, TILESIZE))
            self.sp_button2_7 = SpriteButton(self.game, 260, 600, self.game.dirt_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE))
            self.sp_button2_8 = SpriteButton(self.game, 300, 600, self.game.dirt_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE))
            self.sp_button2_9 = SpriteButton(self.game, 340, 600, self.game.dirt_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE))
            self.sp_button2_10 = SpriteButton(self.game, 380, 600, self.game.dirt_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE))
            self.sp_button2_11 = SpriteButton(self.game, 420, 600, self.game.dirt_spritesheet.get_sprite(320, 32, TILESIZE, TILESIZE))
            self.sp_button2_12 = SpriteButton(self.game, 460, 600, self.game.dirt_spritesheet.get_sprite(352, 32, TILESIZE, TILESIZE))
            self.sp_button2_13 = SpriteButton(self.game, 500, 600, self.game.dirt_spritesheet.get_sprite(384, 32, TILESIZE, TILESIZE))
            self.sp_button2_14 = SpriteButton(self.game, 540, 600, self.game.dirt_spritesheet.get_sprite(416, 32, TILESIZE, TILESIZE))
            self.sp_button2_15 = SpriteButton(self.game, 580, 600, self.game.dirt_spritesheet.get_sprite(448, 32, TILESIZE, TILESIZE))
            self.sp_button2_16 = SpriteButton(self.game, 620, 600, self.game.dirt_spritesheet.get_sprite(480, 32, TILESIZE, TILESIZE))
            self.sp_button2_17 = SpriteButton(self.game, 660, 600, self.game.dirt_spritesheet.get_sprite(512, 32, TILESIZE, TILESIZE))
            self.sp_button2_18 = SpriteButton(self.game, 700, 600, self.game.dirt_spritesheet.get_sprite(544, 32, TILESIZE, TILESIZE))
            self.sp_button2_19 = SpriteButton(self.game, 740, 600, self.game.dirt_spritesheet.get_sprite(576, 32, TILESIZE, TILESIZE))
            self.sp_button2_20 = SpriteButton(self.game, 780, 600, self.game.dirt_spritesheet.get_sprite(608, 32, TILESIZE, TILESIZE))
            self.sp_button2_21 = SpriteButton(self.game, 820, 600, self.blank_32)
            self.sp_button2_22 = SpriteButton(self.game, 860, 600, self.blank_32)
            self.sp_button2_23 = SpriteButton(self.game, 900, 600, self.blank_32)
            self.sp_button2_24 = SpriteButton(self.game, 940, 600, self.blank_32)

        elif self.map_editor.mode == 'furnishings':
            self.sp_button_1 = SpriteButton(self.game, 20, 560, self.game.trench_furnishings_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE))
            self.sp_button_2 = SpriteButton(self.game, 60, 560, self.game.trench_furnishings_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE))
            self.sp_button_3 = SpriteButton(self.game, 100, 560, self.game.trench_furnishings_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE))
            self.sp_button_4 = SpriteButton(self.game, 140, 560, self.game.trench_furnishings_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE))
            self.sp_button_5 = SpriteButton(self.game, 180, 560, self.game.trench_furnishings_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE))
            self.sp_button_6 = SpriteButton(self.game, 220, 560, self.game.trench_furnishings_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE))
            self.sp_button_7 = SpriteButton(self.game, 260, 560, self.game.trench_furnishings_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE))
            self.sp_button_8 = SpriteButton(self.game, 300, 560, self.game.trench_furnishings_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE))
            self.sp_button_9 = SpriteButton(self.game, 340, 560, self.game.trench_furnishings_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE))
            self.sp_button_10 = SpriteButton(self.game, 380, 560, self.game.trench_furnishings_spritesheet.get_sprite(288, 0, TILESIZE, TILESIZE))
            self.sp_button_11 = SpriteButton(self.game, 420, 560, self.game.trench_furnishings_spritesheet.get_sprite(320, 0, TILESIZE, TILESIZE))
            self.sp_button_12 = SpriteButton(self.game, 460, 560, self.game.trench_furnishings_spritesheet.get_sprite(352, 0, TILESIZE, TILESIZE))
            self.sp_button_13 = SpriteButton(self.game, 500, 560, self.game.trench_furnishings_spritesheet.get_sprite(384, 0, TILESIZE, TILESIZE))
            self.sp_button_14 = SpriteButton(self.game, 540, 560, self.game.trench_furnishings_spritesheet.get_sprite(416, 0, TILESIZE, TILESIZE))
            self.sp_button_15 = SpriteButton(self.game, 580, 560, self.game.trench_furnishings_spritesheet.get_sprite(448, 0, TILESIZE, TILESIZE))
            self.sp_button_16 = SpriteButton(self.game, 620, 560, self.game.trench_furnishings_spritesheet.get_sprite(480, 0, TILESIZE, TILESIZE))
            self.sp_button_17 = SpriteButton(self.game, 660, 560, self.blank_32)
            self.sp_button_18 = SpriteButton(self.game, 700, 560, self.blank_32)
            self.sp_button_19 = SpriteButton(self.game, 740, 560, self.blank_32)
            self.sp_button_20 = SpriteButton(self.game, 780, 560, self.blank_32)
            self.sp_button_21 = SpriteButton(self.game, 820, 560, self.blank_32)
            self.sp_button_22 = SpriteButton(self.game, 860, 560, self.blank_32)
            self.sp_button_23 = SpriteButton(self.game, 900, 560, self.blank_32)
            self.sp_button_24 = SpriteButton(self.game, 940, 560, self.blank_32)

            self.sp_button2_1 = SpriteButton(self.game, 20, 600, self.game.trench_furnishings_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE))
            self.sp_button2_2 = SpriteButton(self.game, 60, 600, self.game.trench_furnishings_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE))
            self.sp_button2_3 = SpriteButton(self.game, 100, 600, self.game.trench_furnishings_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE))
            self.sp_button2_4 = SpriteButton(self.game, 140, 600, self.game.trench_furnishings_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE))
            self.sp_button2_5 = SpriteButton(self.game, 180, 600, self.game.trench_furnishings_spritesheet.get_sprite(128, 32, TILESIZE, TILESIZE))
            self.sp_button2_6 = SpriteButton(self.game, 220, 600, self.game.trench_furnishings_spritesheet.get_sprite(160, 32, TILESIZE, TILESIZE))
            self.sp_button2_7 = SpriteButton(self.game, 260, 600, self.game.trench_furnishings_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE))
            self.sp_button2_8 = SpriteButton(self.game, 300, 600, self.game.trench_furnishings_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE))
            self.sp_button2_9 = SpriteButton(self.game, 340, 600, self.game.trench_furnishings_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE))
            self.sp_button2_10 = SpriteButton(self.game, 380, 600, self.game.trench_furnishings_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE))
            self.sp_button2_11 = SpriteButton(self.game, 420, 600, self.game.trench_furnishings_spritesheet.get_sprite(320, 32, TILESIZE, TILESIZE))
            self.sp_button2_12 = SpriteButton(self.game, 460, 600, self.game.trench_furnishings_spritesheet.get_sprite(352, 32, TILESIZE, TILESIZE))
            self.sp_button2_13 = SpriteButton(self.game, 500, 600, self.game.trench_furnishings_spritesheet.get_sprite(384, 32, TILESIZE, TILESIZE))
            self.sp_button2_14 = SpriteButton(self.game, 540, 600, self.game.trench_furnishings_spritesheet.get_sprite(416, 32, TILESIZE, TILESIZE))
            self.sp_button2_15 = SpriteButton(self.game, 580, 600, self.game.trench_furnishings_spritesheet.get_sprite(448, 32, TILESIZE, TILESIZE))
            self.sp_button2_16 = SpriteButton(self.game, 620, 600, self.game.trench_furnishings_spritesheet.get_sprite(480, 32, TILESIZE, TILESIZE))
            self.sp_button2_17 = SpriteButton(self.game, 660, 600, self.blank_32)
            self.sp_button2_18 = SpriteButton(self.game, 700, 600, self.blank_32)
            self.sp_button2_19 = SpriteButton(self.game, 740, 600, self.blank_32)
            self.sp_button2_20 = SpriteButton(self.game, 780, 600, self.blank_32)
            self.sp_button2_21 = SpriteButton(self.game, 820, 600, self.blank_32)
            self.sp_button2_22 = SpriteButton(self.game, 860, 600, self.blank_32)
            self.sp_button2_23 = SpriteButton(self.game, 900, 600, self.blank_32)
            self.sp_button2_24 = SpriteButton(self.game, 940, 600, self.blank_32)

        elif self.map_editor.mode == 'buildings':
            self.sp_button_1 = SpriteButton(self.game, 20, 560, self.game.trench_bunker_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE))
            self.sp_button_2 = SpriteButton(self.game, 60, 560, self.game.trench_bunker_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE))
            self.sp_button_3 = SpriteButton(self.game, 100, 560, self.game.trench_bunker_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE))
            self.sp_button_4 = SpriteButton(self.game, 140, 560, self.game.trench_bunker_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE))
            self.sp_button_5 = SpriteButton(self.game, 180, 560, self.game.trench_bunker_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE))
            self.sp_button_6 = SpriteButton(self.game, 220, 560, self.game.trench_bunker_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE))
            self.sp_button_7 = SpriteButton(self.game, 260, 560, self.game.trench_bunker_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE))
            self.sp_button_8 = SpriteButton(self.game, 300, 560, self.game.houses_spritesheet.get_sprite(0, 0, 64, 64))
            self.sp_button_9 = SpriteButton(self.game, 340, 560, self.blank_32)
            self.sp_button_10 = SpriteButton(self.game, 380, 560, self.game.houses_spritesheet.get_sprite(64, 0, 64, 64))
            self.sp_button_11 = SpriteButton(self.game, 420, 560, self.blank_32)
            self.sp_button_12 = SpriteButton(self.game, 460, 560, self.game.houses_spritesheet.get_sprite(128, 0, 64, 64))
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

        elif self.map_editor.mode == 'surface':
            self.sp_button_1 = SpriteButton(self.game, 20, 560, self.game.water_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE, 128))
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

        elif self.map_editor.mode == 'digging':
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
        except:
            pass
        try:
            self.screen.blit(self.sp_button_4.image, self.sp_button_4.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_5.image, self.sp_button_5.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_6.image, self.sp_button_6.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_7.image, self.sp_button_7.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_8.image, self.sp_button_8.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_9.image, self.sp_button_9.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_10.image, self.sp_button_10.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_11.image, self.sp_button_11.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_12.image, self.sp_button_12.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_13.image, self.sp_button_13.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_14.image, self.sp_button_14.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_15.image, self.sp_button_15.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_16.image, self.sp_button_16.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_17.image, self.sp_button_17.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_18.image, self.sp_button_18.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_19.image, self.sp_button_19.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_20.image, self.sp_button_20.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_21.image, self.sp_button_21.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_22.image, self.sp_button_22.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_23.image, self.sp_button_23.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button_24.image, self.sp_button_24.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_1.image, self.sp_button2_1.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_2.image, self.sp_button2_2.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_3.image, self.sp_button2_3.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_4.image, self.sp_button2_4.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_5.image, self.sp_button2_5.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_6.image, self.sp_button2_6.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_7.image, self.sp_button2_7.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_8.image, self.sp_button2_8.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_9.image, self.sp_button2_9.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_10.image, self.sp_button2_10.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_11.image, self.sp_button2_11.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_12.image, self.sp_button2_12.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_13.image, self.sp_button2_13.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_14.image, self.sp_button2_14.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_15.image, self.sp_button2_15.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_16.image, self.sp_button2_16.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_17.image, self.sp_button2_17.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_18.image, self.sp_button2_18.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_19.image, self.sp_button2_19.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_20.image, self.sp_button2_20.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_21.image, self.sp_button2_21.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_22.image, self.sp_button2_22.rect)
        except:
            pass
        try:
            self.screen.blit(self.sp_button2_23.image, self.sp_button2_23.rect)
        except:
            pass
        try:
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
