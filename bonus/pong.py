# -*- coding: Utf-8 -*

import time
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
        clock = pygame.time.Clock()
        self.count_down(3.0, clock)
        done = False
        while not done:
            clock.tick(60)
            self.draw_screen()
            done = self.events()
        pygame.quit()

    def count_down(self, seconds, clock):
        start_time = time.time()
        actual_time = 0
        while seconds > actual_time:
            clock.tick(60)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                return True
            if (event.type == pygame.KEYUP) and (event.key == pygame.K_RETURN):
                return False
            actual_time = time.time() - start_time
            self.draw_screen()
            self.draw_text(str(int(seconds - actual_time + 1)),
                           size=40,
                           midbottom=(self.screen.centerx, self.screen.bottom - 20))
            pygame.display.update()

    def draw_screen(self):
        self.window.fill(BLACK)
        self.ball.draw(self.window)
        self.player[1].draw(self.window)
        self.player[2].draw(self.window)
        self.draw_text(str(self.score[1]),
                       size=50,
                       midtop=(self.screen.width * 0.25, 0))
        self.draw_text(str(self.score[2]),
                       size=50,
                       midtop=(self.screen.width * 0.75, 0))
        pygame.display.update()

    def draw_text(self, text, size, **kwargs):
        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, size)
        text = font.render(text, 1, WHITE)
        text_rect = text.get_rect(**kwargs)
        self.window.blit(text, text_rect)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        keys = pygame.key.get_pressed()
        for player in self.player.values():
            player.move(self.screen, keys)
        self.ball.move()
        self.check_ball_collision()
        return False

    def check_ball_collision(self):
        for player in self.player.values():
            if pygame.sprite.collide_mask(player, self.ball) is not None \
            and self.ball.centery in range(player.top, player.bottom + 1):
                self.ball.invert_axis("x")
            if pygame.sprite.collide_mask(player, self.ball) is not None \
            and self.ball.centerx in range(player.left, player.right + 1):
                self.ball.invert_axis("y")
        if self.ball.top <= self.screen.top or self.ball.bottom >= self.screen.bottom:
            self.ball.invert_axis("y")
        if (self.ball.left <= self.screen.left) or (self.ball.right >= self.screen.right):
            self.ball.invert_axis("x")
            if self.ball.right >= self.screen.right:
                self.score[1] += 1
            if self.ball.left <= self.screen.top:
                self.score[2] += 1
