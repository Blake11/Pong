import pygame


class Player(object):
    point = 0

    def __init__(self, player_number):
        if player_number == 1:
            self.shape = pygame.Rect(600, 200, 20, 80)
            self.color = (0, 255, 0)
        elif player_number == 2:
            self.shape = pygame.Rect(20, 200, 20, 80)
            self.color = (0, 0, 255)
        self.player_number = player_number

    def get_input(self):
        if self.player_number == 1:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if self.get_y + self.get_height < 470:
                    self.move("down")
            elif pygame.key.get_pressed()[pygame.K_UP]:
                if self.get_y > 10:
                    self.move("up")
        elif self.player_number == 2:
            if pygame.key.get_pressed()[pygame.K_s]:
                if self.get_y + self.get_height < 470:
                    self.move("down")
            elif pygame.key.get_pressed()[pygame.K_w]:
                if self.get_y > 10:
                    self.move("up")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.shape)

    def move(self, direction):
        if direction == "down":
            self.shape = self.shape.move(0, 5)
        elif direction == "up":
            self.shape = self.shape.move(0, -5)
        self.shape = self.shape

    def add_point(self):
        self.point += 1


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
