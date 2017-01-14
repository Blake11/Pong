import pygame
from player import Player
from ball import Ball
from wall import Wall
from colors import *

pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Niggapong')
fps = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 15)
border = [Wall(0, 0, 640, 0), Wall(0, 480, 640, 0), Wall(0,0,0,480), Wall(640,0,0,480)]
player = Player(1)
player2 = Player(2)
ball = Ball()


while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # move handler
    player.get_input()
    player2.get_input()

    score = font.render(str(str(player2.point) + "-" + str(player.point)), 4, WHITE)

    ball.move()
    ball.collide(player.shape)
    ball.collide(player2.shape)
    for i in range(0,len(border)):
        if i == 1 or i == 0:
            ball.collide_wall(border[i].shape)
        else:

            if i == 2 and ball.goal(border[i].shape):
                ball.reset()
                player.add_point()
            elif i == 3 and ball.goal(border[i].shape):
                ball.reset()
                player2.add_point()

            pass


    # clear the screen before drawing
    screen.fill(BLACK) # start new frame
    # drawing goes below

    for wall in border:
        wall.draw(screen)
    player.draw(screen)
    player2.draw(screen)
    ball.draw(screen)
    screen.blit(score, (640/2, 50))
    pygame.display.update() # display frame
    fps.tick(60) # console peasants can't handle my game
