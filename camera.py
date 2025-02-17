import pygame


class Camera:
    def __init__(self, game):
        self.game = game

        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.movement()
        for sprite in self.game.bottom_sprites:
            sprite.rect.y += self.y_change
            sprite.rect.x += self.x_change
        for sprite in self.game.all_sprites:
            sprite.rect.y += self.y_change
            sprite.rect.x += self.x_change
        for sprite in self.game.top_sprites:
            sprite.rect.y += self.y_change
            sprite.rect.x += self.x_change
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y_change += self.game.camera_speed
        if keys[pygame.K_s]:
            self.y_change -= self.game.camera_speed
        if keys[pygame.K_d]:
            self.x_change -= self.game.camera_speed
        if keys[pygame.K_a]:
            self.x_change += self.game.camera_speed
