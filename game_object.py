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

        self.invencible = False
        self.invencible_duration = utils.current_milli_time()
        self.invencible_switch_color = self.color

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
            self.move_pos[0] += move_pixels
        else:
            self.move_pos[1] += move_pixels

    def lose_hp(self, health_points):
        if self.immortal or self.invencible or not self.id in g_game.objects:
            return

        self.health_points -= health_points

        if self.health_points <= 0:
            del g_game.objects[self.id]

    def draw(self):
        if self.rect is None or self.color is None:
            return

        draw_color = self.invencible and self.invencible_switch_color or self.color

        screen = pygame.display.get_surface()

        pygame.draw.rect(screen, draw_color or (0, 0, 0), self.rect)

        if self.invencible:
            self.invencible_switch_color = self.invencible_switch_color == (0, 0, 0) and self.color or (0, 0, 0)

    @abstractmethod
    def update(self):
        pass
    