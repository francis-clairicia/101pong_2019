# -*- coding: Utf-8 -*

import pygame
from player import Player
from ball import Ball

pygame.init()
pygame.key.set_repeat(30, 10)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Pong:
    def __init__(self, width=800, height=600):
        size = (width, height)
        self.window = pygame.display.set_mode(size)
        self.screen = self.window.get_rect()
        self.player = {1:Player([15, 90], WHITE, midleft=self.screen.midleft),
                       2:Player([15, 90], WHITE, midright=self.screen.midright)}
        self.player[1].set_keys(pygame.K_z, pygame.K_s)
        self.player[2].set_keys(pygame.K_UP, pygame.K_DOWN)
        self.score = {1: 0, 2: 0}
        self.ball = Ball(20, WHITE, center=self.screen.center)

    def run(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(60)
            self.draw_screen()
            done = self.events()
        pygame.quit()

    def draw_screen(self):
        self.window.fill(BLACK)
        self.ball.draw(self.window)
        self.player[1].draw(self.window)
        self.player[2].draw(self.window)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        keys = pygame.key.get_pressed()
        for player in self.player.values():
            player.move(self.screen, keys)
        self.ball.move(self.screen, self.score)
        self.check_ball_collision()
        return False

    def check_ball_collision(self):
        for player in self.player.values():
            if pygame.sprite.collide_mask(player, self.ball) is not None \
            and self.ball.rect.centery in range(player.rect.top, player.rect.bottom + 1):
                self.ball.invert_axis("x")
                self.ball.increase_speed()
