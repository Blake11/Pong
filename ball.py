import pygame
from random import randint
from colors import *


class Ball(object):
    shape = pygame.Rect(640/2,480/2,20,20)
    color = RED
    velocity = [0,0]

    def __init__(self):
        self.random_velocity()

    def random_velocity(self):
        x = randint(-10, 10)
        self.velocity[0] = x
        y = randint(-3, 3)
        self.velocity[1] = y

    def reset(self):
        self.shape = pygame.Rect(640/2,480/2,20,20).copy()
        self.random_velocity()

    def draw(self,screen):
        pygame.draw.ellipse(screen, self.color, self.shape)

    def move(self):
        self.shape = self.shape.move(self.velocity[0], self.velocity[1])

    def collide(self, player):
        if player.colliderect(self.shape):
            self.velocity[0] *= -1

    def collide_wall(self,wall):
        if wall.colliderect(self.shape):
            self.velocity[1] *= -1

    def goal(self,wall):
        if wall.colliderect(self.shape):
            return True
        else:
            return False

    @property
    def get_x(self):
        return self.shape[0]

    @property
    def get_y(self):
        return self.shape[1]

    @property
    def get_width(self):
        return self.shape[2]

    @property
    def get_height(self):
        return self.shape[3]
