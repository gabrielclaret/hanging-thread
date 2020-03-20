from abc import ABC, abstractmethod
from game import g_game
import pygame

g_id = 0

class GameObject(ABC):
    def __init__(self, x, y, color, width, height, collision_behavior = None, immortal = False):
        global g_id
        self.id = g_id
        g_id += 1

        screen = pygame.display.get_surface()

        self.rect = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        self.area = screen.get_rect()

        self.color = color

        self.collision_behavior = collision_behavior
        
        self.immortal = immortal

        # TODO
        self.health_points = 100

        g_game.objects[self.id] = self

    def draw(self):
        if self.rect is None or self.color is None:
            return

        screen = pygame.display.get_surface()

        pygame.draw.rect(screen, self.color or (0, 0, 0), self.rect)

    @abstractmethod
    def update(self):
        pass
    