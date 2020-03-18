from game import g_game
from game_object import GameObject
from monster import Monster
from gplatform import Platform
from player import Player
import pygame

def can_attack(creature_a, creature_b):
    return (isinstance(creature_a, Player) and isinstance(creature_b, Monster)) or (isinstance(creature_a, Monster) and isinstance(creature_b, Player))

class Projectile(GameObject):
    def __init__(self, range, speed, color, width, height, start_x, start_y, direction, shooter):
        super(Projectile, self).__init__()

        screen = pygame.display.get_surface()
        
        self.rect = pygame.draw.rect(screen, color, pygame.Rect(start_x, start_y, width, height))
        self.area = screen.get_rect()

        self.range = range
        self.speed = speed
        self.color = color
        self.direction = direction
        self.shooter = shooter

    def update(self):
        move_pos = [self.direction * self.speed, 0]

        self.range -= self.speed

        new_rect = self.rect.move(move_pos)

        if self.range <= 0:
            del g_game.objects[self.id]

        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            if not new_rect.colliderect(obj.rect):
                continue
            elif isinstance(obj, Platform) or can_attack(self.shooter, obj):
                print("Hit something!")
                del g_game.objects[self.id]

                break

        self.rect = new_rect

        pygame.event.pump()