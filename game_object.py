from abc import ABC, abstractmethod
from game import g_game
import pygame
import utils

g_id = 0

class GameObject(ABC):
    def __init__(self, x, y, speed, color, width, height, direction, horizontal, collision_behavior = None, immortal = False):
        global g_id
        self.id = g_id
        g_id += 1

        screen = pygame.display.get_surface()

        self.rect = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        self.area = screen.get_rect()

        self.speed = speed
        self.color = color
        self.direction = direction
        self.horizontal = horizontal

        self.collision_behavior = collision_behavior

        self.immortal = immortal

        self.move_pos = [0, 0]
        self.state = utils.STILL

        # TODO
        self.health_points = 100

        g_game.objects[self.id] = self

    def move(self, direction):
        move_pixels = direction * self.speed

        if self.horizontal:
            self.move_pos[0] = move_pixels
        else:
            self.move_pos[1] = move_pixels

        self.direction = direction
        self.state = utils.MOVING

    def move_as(self, reference):
        move_pixels = reference.direction * reference.speed

        if reference.horizontal:
            self.move_pos[0] = move_pixels
        else:
            self.move_pos[1] = move_pixels

    def draw(self):
        if self.rect is None or self.color is None:
            return

        screen = pygame.display.get_surface()

        pygame.draw.rect(screen, self.color or (0, 0, 0), self.rect)

    @abstractmethod
    def update(self):
        pass
    