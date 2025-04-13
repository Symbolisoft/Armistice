import pygame

from ui_elements.map_editor_ui import *
from map_translator import *
from sprites.dirt import *
from sprites.map_editor_trench import *
from sprites.map_editor_furniture import *

class MapEditor:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

        self.mode = 'None'
        

        self.game.map_editor_open = True

        #   self.camera_limits = camera_block_map_translator(self.game, 'data/maps/map_editor_camera_limits.amf')
        self.game.map_bottom = ground_map_translator(self.game, 'data/maps/map_editor_bottom_layer.amf')
        self.game.map_start = ground_map_translator(self.game, 'data/maps/map_editor_start.amf')

        self.map_ui = MapUI(self.game, self)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.game.map_editor_open = False
                self.game.main_menu()

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    if self.game.zoom_level < 1.8:
                        self.game.zoom_level += 0.05
                    else: 
                        self.game.zoom_level = 1.8
                if event.y < 0:
                    if self.game.zoom_level > 0.9:
                        self.game.zoom_level -= 0.05
                    else:
                        self.game.zoom_level = 0.9

            

        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_UP]:
            if self.game.zoom_level < 1.8:
                self.game.zoom_level += 0.05
            else: 
                self.game.zoom_level = 1.8
        if keys[pygame.K_DOWN]:
            if self.game.zoom_level > 0.9:
                self.game.zoom_level -= 0.05
            else:
                self.game.zoom_level = 0.9

        if keys[pygame.K_LSHIFT]:
            self.game.camera_speed = self.game.camera_speed * 2
        else:
            self.game.camera_speed = self.game.camera_speed

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            if self.mode == 'trench walls':
                self.game.zoom_level = 1
                if self.map_ui.build_sprite == 0:
                    pass
                elif self.map_ui.build_sprite == 1:
                    MapEdTrench1(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 2:
                    MapEdTrench2(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 3:
                    MapEdTrench3(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 4:
                    MapEdTrench4(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 5:
                    MapEdTrench5(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 6:
                    MapEdTrench6(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 7:
                    MapEdTrench7(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 8:
                    MapEdTrench8(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 9:
                    MapEdTrench9(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 10:
                    MapEdTrench10(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 11:
                    MapEdTrench11(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 12:
                    MapEdTrench12(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 13:
                    MapEdTrench13(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 14:
                    MapEdTrench14(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 15:
                    MapEdTrench15(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 16:
                    MapEdTrench16(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 17:
                    MapEdTrench17(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 18:
                    MapEdTrench18(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 19:
                    MapEdTrench19(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0

                elif self.map_ui.build_sprite == 25:
                    MapEdTrench25(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 26:
                    MapEdTrench26(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 27:
                    MapEdTrench27(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 28:
                    MapEdTrench28(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 29:
                    MapEdTrench29(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 30:
                    MapEdTrench30(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 31:
                    MapEdTrench31(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 32:
                    MapEdTrench32(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 33:
                    MapEdTrench33(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 34:
                    MapEdTrench34(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 35:
                    MapEdTrench35(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 36:
                    MapEdTrench36(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 37:
                    MapEdTrench37(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 38:
                    MapEdTrench38(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 39:
                    MapEdTrench39(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 40:
                    MapEdTrench40(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0

            if self.mode == 'furnishings':
                self.game.zoom_level = 1
                if self.map_ui.build_sprite == 0:
                    pass
                elif self.map_ui.build_sprite == 41:
                    MapEdBunkRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 42:
                    MapEdSandBagsSmallRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 43:
                    MapEdSandBagsLargeRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 44:
                    MapEdCabinetRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 45:
                    MapEdGunRackRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 46:
                    MapEdGreenCratesRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 47:
                    MapEdArtyShellsRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 48:
                    MapEdFiringStepRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 49:
                    MapEdBarbedWireRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 50:
                    MapEdLadderRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 51:
                    MapEdBarrelsRight(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0

                elif self.map_ui.build_sprite == 65:
                    MapEdBunkLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 66:
                    MapEdSandBagsSmallLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 67:
                    MapEdSandBagsLargeLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 68:
                    MapEdCabinetLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 69:
                    MapEdGunRackLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 70:
                    MapEdGreenCratesLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 71:
                    MapEdArtyShellsLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 72:
                    MapEdFiringStepLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 73:
                    MapEdBarbedWireLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 74:
                    MapEdLadderLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0
                elif self.map_ui.build_sprite == 75:
                    MapEdBarrelsLeft(self.game, mouse_pos[0], mouse_pos[1])
                    self.map_ui.build_sprite = 0

        if mouse_pressed[2]:
            sprites = []
            for sprite in self.game.dirt_group:
                for tile in self.game.active_tile_group:
                    self.game.digging_sounds[random.randint(0, 2)].play(0)
                    if sprite.rect.collidepoint(tile.rect.x+(TILESIZE/2), tile.rect.y+(TILESIZE/2)):
                        sprites.append(sprite)
                        
            try:            
                sprites[0].kill()
            except IndexError:
                pass
            
            sprites.clear()

        

        
        self.map_ui.events()

    def update(self):
        self.game.bottom_sprites.update()
        self.game.all_sprites.update()
        self.game.top_sprites.update()
        self.game.camera.update()
        self.map_ui.update()
        self.game.map_editor_build_sprite.update()


        if self.game.zoom_level > 1.8:
            self.game.zoom_level = 1.8
        elif self.game.zoom_level < 0.9:
            self.game.zoom_level = 0.9

        self.game.camera_speed = self.game.camera_speed/(self.game.zoom_level)
        if self.game.camera_speed >= 8:
            self.game.camera_speed = 8
        if self.game.camera_speed <= 4:
            self.game.camera_speed = 4

        if self.mode == 'None' or self.mode == 'digging':
            self.game.mouse = self.game.default_mouse
        elif self.mode == 'trench walls':
            if self.map_ui.build_sprite == 1:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 2:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 3:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 4:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 5:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 6:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 7:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 8:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 9:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 10:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(288, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 11:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(320, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 12:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(352, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 13:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(384, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 14:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(416, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 15:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(448, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 16:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(480, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 17:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(512, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 18:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(544, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 19:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(576, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 25:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 26:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 27:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 28:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 29:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(128, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 30:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(160, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 31:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 32:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 33:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 34:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 35:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(320, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 36:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(352, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 37:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(384, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 38:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(416, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 39:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(448, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 40:
                self.game.mouse = pygame.transform.scale_by(self.game.dirt_spritesheet.get_sprite(480, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            else:
                self.game.mouse = self.game.default_mouse
        elif self.mode == 'furnishings':
            if self.map_ui.build_sprite == 0:
                self.game.mouse = self.game.default_mouse
            if self.map_ui.build_sprite == 41:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 42:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 43:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 44:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(96, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 45:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(128, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 46:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(160, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 47:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(192, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 48:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(224, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 49:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(256, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 50:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(288, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 51:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(320, 0, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 52:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(352, 0, TILESIZE, TILESIZE), self.game.zoom_level)

            elif self.map_ui.build_sprite == 65:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 66:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 67:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 68:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(96, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 69:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(128, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 70:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(160, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 71:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 72:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 73:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 74:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 75:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(320, 32, TILESIZE, TILESIZE), self.game.zoom_level)
            elif self.map_ui.build_sprite == 76:
                self.game.mouse = pygame.transform.scale_by(self.game.trench_furnishings_spritesheet.get_sprite(352, 32, TILESIZE, TILESIZE), self.game.zoom_level)

        

    def draw(self):
        self.screen.fill(BLACK)

        for sprite in self.game.bottom_sprites:
            self.game.minimap_buffer.blit(sprite.image, sprite.rect)
            if self.screen.get_rect().colliderect(sprite.rect):
                #   self.screen_buffer.blit(sprite.image, sprite.rect)
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.game.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.game.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.game.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.game.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.game.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

                if self.mode == 'digging':

                    if sprite == Dirt1 or Dirt2 or TrenchLeftRecess or TrenchRightRecess or TrenchLeftTaperTop or TrenchRightTaperBottom or TrenchLeftTaperBottom or TrenchRightTaperTop or TrenchWalls1:
                        mouse_pos = pygame.mouse.get_pos()
                        hits = scaled_rect.collidepoint(mouse_pos)
                        if hits:
                        
                            ActiveTile(self.game, sprite.rect.x+sprite.x_dif, sprite.rect.y+sprite.y_dif)

        for sprite in sorted(self.game.all_sprites, key= lambda sprite: sprite.rect.centery):
            self.game.minimap_buffer.blit(sprite.image, sprite.rect)
            if self.screen.get_rect().colliderect(sprite.rect):
                #   
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.game.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.game.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.game.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.game.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.game.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

                if self.mode == 'digging':

                    if sprite == Dirt1 or Dirt2 or TrenchLeftRecess or TrenchRightRecess or TrenchLeftTaperTop or TrenchRightTaperBottom or TrenchLeftTaperBottom or TrenchRightTaperTop or TrenchWalls1:
                        mouse_pos = pygame.mouse.get_pos()
                        hits = scaled_rect.collidepoint(mouse_pos)
                        if hits:
                        
                            ActiveTile(self.game, sprite.rect.x+sprite.x_dif, sprite.rect.y+sprite.y_dif)

        for sprite in sorted(self.game.top_sprites, key= lambda sprite: sprite.rect.centery):
            self.game.minimap_buffer.blit(sprite.image, sprite.rect)
            if self.screen.get_rect().colliderect(sprite.rect):
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.game.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.game.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.game.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.game.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.game.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)
        

        self.map_ui.draw()
        mouse_pos = pygame.mouse.get_pos()

        if self.game.unit_attack:
            self.screen.blit(self.game.mouse, (mouse_pos[0]-16, mouse_pos[1]-16))
        elif self.game.unit_move:
            self.screen.blit(self.game.mouse, (mouse_pos[0]-16, mouse_pos[1]-16))
        else:
            self.screen.blit(self.game.mouse, mouse_pos)

        self.game.clock.tick(FPS)
        pygame.display.update()

    def loop(self):
        self.events()
        self.update()
        self.draw()