import pygame


import random

from configs.sprites_config import *
from configs.screen_config import TILESIZE
from sprites.active_tile import *


class TrenchWalls1(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.y = (y-24)*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.dirt_spritesheet.get_sprite(192, 32, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(224, 32, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(256, 32, TILESIZE, TILESIZE),
            self.game.dirt_spritesheet.get_sprite(288, 32, TILESIZE, TILESIZE)     
                       ]
        
        self.image = self.images[random.randint(0, 3)]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.active_timer = pygame.time.get_ticks()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()
        click_2 = pygame.mouse.get_pressed()

        self.collide_mouse(mouse_pos)

    def collide_mouse(self, pos):
        hits = self.rect.collidepoint(pos)
        if hits:
            if self.game.digging:
                now = pygame.time.get_ticks()
                if now - self.active_timer >= 200:
                    ActiveTile(self.game, self.x, self.y)
                    self.active_timer = now


class TrenchLeftTaperTop(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.y = (y-24)*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.dirt_spritesheet.get_sprite(480, 32, TILESIZE, TILESIZE)     
                       ]
        
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.active_timer = pygame.time.get_ticks()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()
        click_2 = pygame.mouse.get_pressed()

        self.collide_mouse(mouse_pos)

    def collide_mouse(self, pos):
        hits = self.rect.collidepoint(pos)
        if hits:
            if self.game.digging:
                now = pygame.time.get_ticks()
                if now - self.active_timer >= 200:
                    ActiveTile(self.game, self.x, self.y)
                    self.active_timer = now


class TrenchLeftTaperBottom(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.y = (y-24)*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.dirt_spritesheet.get_sprite(448, 32, TILESIZE, TILESIZE)     
                       ]
        
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.active_timer = pygame.time.get_ticks()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()
        click_2 = pygame.mouse.get_pressed()

        self.collide_mouse(mouse_pos)

    def collide_mouse(self, pos):
        hits = self.rect.collidepoint(pos)
        if hits:
            if self.game.digging:
                now = pygame.time.get_ticks()
                if now - self.active_timer >= 200:
                    ActiveTile(self.game, self.x, self.y)
                    self.active_timer = now


class TrenchLeftRecess(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.y = (y-24)*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.dirt_spritesheet.get_sprite(416, 32, TILESIZE, TILESIZE)     
                       ]
        
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.active_timer = pygame.time.get_ticks()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()
        click_2 = pygame.mouse.get_pressed()

        self.collide_mouse(mouse_pos)

    def collide_mouse(self, pos):
        hits = self.rect.collidepoint(pos)
        if hits:
            if self.game.digging:
                now = pygame.time.get_ticks()
                if now - self.active_timer >= 200:
                    ActiveTile(self.game, self.x, self.y)
                    self.active_timer = now


class TrenchRightTaperTop(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.y = (y-24)*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.dirt_spritesheet.get_sprite(384, 32, TILESIZE, TILESIZE)     
                       ]
        
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.active_timer = pygame.time.get_ticks()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()
        click_2 = pygame.mouse.get_pressed()

        self.collide_mouse(mouse_pos)

    def collide_mouse(self, pos):
        hits = self.rect.collidepoint(pos)
        if hits:
            if self.game.digging:
                now = pygame.time.get_ticks()
                if now - self.active_timer >= 200:
                    ActiveTile(self.game, self.x, self.y)
                    self.active_timer = now


class TrenchRightTaperBottom(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.y = (y-24)*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.dirt_spritesheet.get_sprite(320, 32, TILESIZE, TILESIZE)     
                       ]
        
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.active_timer = pygame.time.get_ticks()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()
        click_2 = pygame.mouse.get_pressed()

        self.collide_mouse(mouse_pos)

    def collide_mouse(self, pos):
        hits = self.rect.collidepoint(pos)
        if hits:
            if self.game.digging:
                now = pygame.time.get_ticks()
                if now - self.active_timer >= 200:
                    ActiveTile(self.game, self.x, self.y)
                    self.active_timer = now


class TrenchRightRecess(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER_2
        self.groups = self.game.all_sprites, self.game.dirt_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = (x-16)*TILESIZE
        self.y = (y-24)*(TILESIZE/2)
        self.width = TILESIZE
        self.height = TILESIZE

        self.images = [
            self.game.dirt_spritesheet.get_sprite(352, 32, TILESIZE, TILESIZE)     
                       ]
        
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.active_timer = pygame.time.get_ticks()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()
        click_2 = pygame.mouse.get_pressed()

        self.collide_mouse(mouse_pos)

    def collide_mouse(self, pos):
        hits = self.rect.collidepoint(pos)
        if hits:
            if self.game.digging:
                now = pygame.time.get_ticks()
                if now - self.active_timer >= 200:
                    ActiveTile(self.game, self.x, self.y)
                    self.active_timer = now


