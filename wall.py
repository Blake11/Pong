import pygame
from colors import *


class Wall(object):

    def __init__(self, x, y, width, height):
        self.shape = pygame.Rect(x, y, width, height)

    def draw(self,screen):
        pygame.draw.rect(screen, WHITE, self.shape, 20)

