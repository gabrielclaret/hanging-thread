from game import g_game
from game_object import GameObject
from monster import Monster
from leveler import Leveler
from player import Player
import pygame
import utils

def can_attack(attacker, target):
    return isinstance(attacker, Player) or (not isinstance(attacker, Player) and isinstance(target, Player))

class Projectile(GameObject):
    def __init__(self, start_x, start_y, range, speed, color, width, height, direction, shooter, horizontal = True, collision_behavior = utils.IGNORE_ALWAYS, immortal = True):
        super(Projectile, self).__init__(start_x, start_y, speed, color, width, height, direction, horizontal, collision_behavior, immortal)

        self.range = range
        self.direction = direction
        self.shooter = shooter

    def update(self):
        self.move(self.direction)

        self.range -= self.speed

        new_rect = self.rect.move(self.move_pos)

        if self.range <= 0:
            del g_game.objects[self.id]

        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            if not new_rect.colliderect(obj.rect):
                continue
            elif can_attack(self.shooter, obj) or isinstance(obj, Leveler):
                # lose hp
                # obj.lose_hp

                del g_game.objects[self.id]

                break

        self.rect = new_rect

        pygame.event.pump()