from abc import ABC, abstractmethod
from game import g_game
import pygame
import utils

g_id = 0

class GameObject(ABC):
    def __init__(self, x, y, speed, color, width, height, direction, horizontal, max_health_points, immortal = False, collision_behavior = utils.DO_NOT_IGNORE):
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

        self.health_points = max_health_points
        self.max_health_points = max_health_points

        g_game.objects[self.id] = self

    def move(self, direction):
        move_pixels = direction * self.speed

        if self.horizontal:
            self.move_pos[0] = move_pixels
        else:
            self.move_pos[1] = move_pixels

        self.direction = direction

    def move_as(self, reference):
        move_pixels = reference.direction * reference.speed

        if reference.horizontal:
            self.move_pos[0] += move_pixels
        else:
            self.move_pos[1] += move_pixels

    def lose_health(self, health_points):
        if self.immortal or self.invencible or not self.id in g_game.objects:
            return

        print(f"{self.id} lost {health_points} health points...")

        self.health_points -= health_points

        if self.health_points <= 0:
            print(f"{self.id} has died...")
            self.die()

    def draw(self):
        self_rect = self.rect
        self_color = self.color

        if self_rect is None or self_color is None:
            return

        draw_color = self.invencible and self.invencible_switch_color or self_color

        screen = pygame.display.get_surface()

        pygame.draw.rect(screen, draw_color or (0, 0, 0), self_rect)

        if not self.immortal:
            total_width = self.rect.width

            width_health_remaining = (((self.health_points * 100) / self.max_health_points) * total_width) / 100
            health_remaining_rect = pygame.Rect(self_rect.left, self_rect.top - 30, width_health_remaining, 20)
            pygame.draw.rect(screen, (255, 0, 0), health_remaining_rect)

            if width_health_remaining != total_width:
                width_health_lost = total_width - width_health_remaining
                health_lost_rect = pygame.Rect(health_remaining_rect.right, self_rect.top - 30, width_health_lost, 20)
                pygame.draw.rect(screen, (0, 0, 0), health_lost_rect, 1)

        if self.invencible:
            self.invencible_switch_color = self.invencible_switch_color == (0, 0, 0) and self_color or (0, 0, 0)

    def die(self):
        self_id = self.id

        if not self_id in g_game.objects:
            return

        del g_game.objects[self_id]

    @abstractmethod
    def update(self):
        pass
    