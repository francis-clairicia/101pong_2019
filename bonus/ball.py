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
        self.move_speed = 1
        self.direction = {"x":random.choice([-2, 2]),
                          "y":random.choice([-2, -1, 1, 2])}

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, screen, score):
        self.rect = self.rect.move(self.direction["x"] + self.move_speed,
                                   self.direction["y"] + self.move_speed)
        if self.rect.top <= screen.top or self.rect.bottom >= screen.bottom:
            self.invert_axis("y")
        if (self.rect.left <= screen.left) or (self.rect.right >= screen.right):
            self.invert_axis("x")
            if self.rect.right >= screen.right:
                score[1] += 1
            if self.rect.left <= screen.top:
                score[2] += 1

    def invert_axis(self, axis):
        self.direction[axis] = -self.direction[axis]

    def increase_speed(self):
        self.move_speed += 0.5
