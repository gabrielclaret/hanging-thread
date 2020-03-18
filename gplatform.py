from game import g_game
from game_object import GameObject
import pygame

class Platform(GameObject):
    def __init__(self, x, y, width, height, color):
        super(Platform, self).__init__()

        screen = pygame.display.get_surface()

        self.rect = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        self.area = screen.get_rect()

        self.color = color

        g_game.objects[self.id] = self

    def update(self):
        pass