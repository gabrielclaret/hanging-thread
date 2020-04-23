from game import g_game
from game_object import GameObject
from monster import Monster
from leveler import Leveler
from player import Player
import pygame
import utils

def can_attack(attacker, target):
    return (isinstance(attacker, Player) and not target.immortal) or (not isinstance(attacker, Player) and isinstance(target, Player) and not target.invencible)

class Projectile(GameObject):
    def __init__(self, attack, start_x, start_y, range, speed, color, width, height, direction, shooter, max_health_points = 1, horizontal = True, immortal = True, collision_behavior = utils.IGNORE_ALWAYS, sprite = "data/sprites/projectile.png"):
        super().__init__(start_x, start_y, speed, color, width, height, direction, horizontal, max_health_points, immortal, collision_behavior, sprite)

        self.attack = attack
        self.range = range
        self.direction = direction
        self.shooter = shooter

    def update(self):
        self.move(self.direction)

        self.range -= self.speed

        new_rect = self.rect.move(self.move_pos)

        if self.range <= 0:
            self.die()

        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            if not new_rect.colliderect(obj.rect):
                continue
            elif (can_attack(self.shooter, obj) or isinstance(obj, Leveler)) and self.id in g_game.objects:
                obj.lose_health(self.attack)

                self.die()

                break

        self.rect = new_rect

        pygame.event.pump()