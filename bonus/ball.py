# -*- coding: Utf-8 -*

import random
import pygame

pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self, diameter, color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        radius = diameter // 2
        circle_size = (diameter, diameter)
        circle_center = (circle_size[0] // 2, circle_size[1] // 2)
        self.image = pygame.Surface(circle_size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(**kwargs)
        pygame.draw.circle(self.image, color, circle_center, radius)
        self.mask = pygame.mask.from_surface(self.image)
        self.move_speed = 3
        self.direction = {"x":random.choice([-2, 2]),
                          "y":random.choice([-2, -1, 1, 2])}

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        move_x = self.direction["x"] * self.move_speed
        move_y = self.direction["y"] * self.move_speed
        self.rect = self.rect.move(move_x, move_y)

    def invert_axis(self, axis):
        self.direction[axis] = -self.direction[axis]

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
