from creature import Creature
from game import g_game
import pygame
from threading import Thread
import utils

class Monster(Creature):
    def __init__(self, x, y, speed, color, width, height, direction, shoot_cooldown, shoot_pattern, walk_pattern, collision_behavior = None, immortal = False):
        super(Monster, self).__init__(x, y, speed, color, width, height, direction, collision_behavior, immortal)

        self.internal_cooldown = utils.current_milli_time() + shoot_cooldown
        self.shoot_cooldown = shoot_cooldown

        self.shoot_pattern = shoot_pattern
        self.shoot_pattern.shooter = self

        self.walk_pattern = walk_pattern
        self.walk_pattern.walker = self

        self.clock = pygame.time.Clock()

        thread = Thread(target = self.__think)
        thread.start()

    def __think(self):
        while g_game.running:
            self.walk_pattern.step()

            if (utils.current_milli_time() - self.internal_cooldown) >= self.shoot_cooldown:
                self.shoot_pattern.fire()

                self.cooldown = utils.current_milli_time() + self.shoot_cooldown

            self.clock.tick(60)