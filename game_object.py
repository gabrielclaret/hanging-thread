from abc import ABC, abstractmethod
import pygame

g_id = 0

class GameObject(ABC):
    def __init__(self):
        global g_id
        self.id = g_id
        g_id += 1

        self.rect = None
        self.color = None

        # TODO
        self.health_points = 100

    def draw(self):
        if self.rect is None or self.color is None:
            return

        screen = pygame.display.get_surface()

        pygame.draw.rect(screen, self.color or (0, 0, 0), self.rect)

    @abstractmethod
    def update(self):
        pass
    