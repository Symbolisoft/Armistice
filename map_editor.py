import pygame

from ui_elements.map_editor_ui import *
from map_translator import *
from sprites.dirt import *

class MapEditor:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

        self.game.map_editor_open = True

        self.game.map_bottom = ground_map_translator(self.game, 'data/maps/map_editor_bottom_layer.amf')
        self.game.map_start = ground_map_translator(self.game, 'data/maps/map_editor_start.amf')

        self.map_ui = MapUI(self.game)

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
        if keys[pygame.K_b]:
            self.game.digging = True
        else:
            self.game.digging = False

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

        if mouse_pressed[2]:
            for sprite in self.game.dirt_group:
                for tile in self.game.active_tile_group:
                    if sprite.rect.collidepoint(tile.rect.x+(TILESIZE/2), tile.rect.y+(TILESIZE/4)):
                        Dirt1(self.game, (sprite.rect.x+sprite.x_dif)/TILESIZE, (sprite.rect.y+sprite.y_dif)/(TILESIZE/2))
                        sprite.kill()

        

        
        self.map_ui.events()

    def update(self):
        self.game.bottom_sprites.update()
        self.game.all_sprites.update()
        self.game.top_sprites.update()
        self.game.camera.update()


        if self.game.zoom_level > 1.8:
            self.game.zoom_level = 1.8
        elif self.game.zoom_level < 0.9:
            self.game.zoom_level = 0.9

        self.game.camera_speed = self.game.camera_speed/(self.game.zoom_level)
        if self.game.camera_speed >= 8:
            self.game.camera_speed = 8
        if self.game.camera_speed <= 4:
            self.game.camera_speed = 4

        
        self.game.mouse = self.game.default_mouse

        
        self.map_ui.update()

    def draw(self):
        self.screen.fill(BLACK)
        
        
        for sprite in self.game.bottom_sprites:
            if self.screen.get_rect().colliderect(sprite.rect):
                #   self.screen_buffer.blit(sprite.image, sprite.rect)
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.game.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.game.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.game.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.game.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.game.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

        for sprite in sorted(self.game.all_sprites, key= lambda sprite: sprite.rect.centery):
            if self.screen.get_rect().colliderect(sprite.rect):
                #   self.screen_buffer.blit(sprite.image, sprite.rect)
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.game.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.game.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.game.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.game.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.game.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

                if sprite == Dirt1 or Dirt2 or TrenchLeftRecess or TrenchRightRecess or TrenchLeftTaperTop or TrenchRightTaperBottom or TrenchLeftTaperBottom or TrenchRightTaperTop or TrenchWalls1:
                    mouse_pos = pygame.mouse.get_pos()
                    hits = scaled_rect.collidepoint(mouse_pos)
                    if hits:
                       
                        ActiveTile(self.game, sprite.rect.x+sprite.x_dif, sprite.rect.y+sprite.y_dif)

        for sprite in sorted(self.game.top_sprites, key= lambda sprite: sprite.rect.centery):
            if self.screen.get_rect().colliderect(sprite.rect):
                scaled_rect = sprite.rect.copy()
                scaled_rect.width = int(sprite.rect.width*self.game.zoom_level)
                scaled_rect.height = int(sprite.rect.height*self.game.zoom_level)
                scaled_rect.x = int(sprite.rect.x*self.game.zoom_level)
                scaled_rect.y = int(sprite.rect.y*self.game.zoom_level)
                scaled_sprite = pygame.transform.scale_by(sprite.image, self.game.zoom_level)
                self.screen.blit(scaled_sprite, scaled_rect)

        self.map_ui.draw()

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