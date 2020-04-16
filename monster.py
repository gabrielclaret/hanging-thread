from creature import Creature
from game import g_game
import pygame
from threading import Thread
import utils

class Monster(Creature):
    def __init__(self, x, y, speed, color, width, height, weight, direction, attack, max_health_points, shoot_cooldown, shoot_pattern, walk_pattern, horizontal = True, immortal = False, collision_behavior = utils.DO_NOT_IGNORE, sprite = "data/sprites/player.png"):
        super().__init__(x, y, speed, color, width, height, direction, attack, max_health_points, shoot_cooldown, shoot_pattern, horizontal, immortal, collision_behavior, sprite)

        self.weight = weight

        self.walk_pattern = walk_pattern
        self.walk_pattern.walker = self

        self.clock = pygame.time.Clock()

        g_game.monster_weight += self.weight

        thread = Thread(target = self.__think)
        thread.start()

    def die(self):
        super().die()

        g_game.monster_weight -= self.weight

    def update(self):
        collision = super().update()

        if not collision[0]:
            return

        if self.walk_pattern.steps_remaining > 0:
            self.direction *= -1
            self.walk_pattern.steps_remaining = self.walk_pattern.steps

    def __think(self):
        self_id = self.id

        while self_id in g_game.objects:
            self.walk_pattern.step()

            if (utils.current_milli_time() - self.internal_cooldown) >= 0:
                self.shoot_pattern.fire()

                self.internal_cooldown = utils.current_milli_time() + self.shoot_cooldown

            self.clock.tick(60)