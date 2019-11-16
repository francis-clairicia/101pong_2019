# -*- coding: Utf-8 -*

import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, size, color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(**kwargs)
        self.mask = pygame.mask.from_surface(self.image)
        self.key_to_up = 0
        self.key_to_down = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_keys(self, key_to_up, key_to_down):
        self.key_to_up = key_to_up
        self.key_to_down = key_to_down

    def move(self, screen, keys):
        if keys[self.key_to_up]:
            self.rect = self.rect.move(0, -6)
        if keys[self.key_to_down]:
            self.rect = self.rect.move(0, 6)
        self.rect.top = screen.top if self.rect.top < screen.top else self.rect.top
        self.rect.bottom = screen.bottom if self.rect.bottom > screen.bottom else self.rect.bottom

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    @property
    def centerx(self):
        return self.rect.centerx

    @property
    def centery(self):
        return self.rect.centery
